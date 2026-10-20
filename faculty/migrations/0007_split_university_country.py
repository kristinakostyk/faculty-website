from django.db import migrations


def split_university_country(apps, schema_editor):
    ExchangeProgram = apps.get_model('faculty', 'ExchangeProgram')

    data = {
        'Uniwersytet Warszawski, Польща':
            ('Uniwersytet Warszawski', 'Польща'),

        'KU Leuven (Бельгія)':
            ('KU Leuven', 'Бельгія'),

        'Vilnius University, Литва':
            ('Vilnius University', 'Литва'),

        'Uniwersytet Jagielloński, Польща':
            ('Uniwersytet Jagielloński', 'Польща'),

        'University of Tartu - Естонія':
            ('University of Tartu', 'Естонія'),

        'Masaryk University, Чехія':
            ('Masaryk University', 'Чехія'),
    }

    for program in ExchangeProgram.objects.all():
        if program.university in data:
            university, country = data[program.university]

            program.university = university
            program.country = country

            program.save(
                update_fields=['university', 'country']
            )


def restore_university_country(apps, schema_editor):
    ExchangeProgram = apps.get_model('faculty', 'ExchangeProgram')

    data = {
        ('Uniwersytet Warszawski', 'Польща'):
            'Uniwersytet Warszawski, Польща',

        ('KU Leuven', 'Бельгія'):
            'KU Leuven (Бельгія)',

        ('Vilnius University', 'Литва'):
            'Vilnius University, Литва',

        ('Uniwersytet Jagielloński', 'Польща'):
            'Uniwersytet Jagielloński, Польща',

        ('University of Tartu', 'Естонія'):
            'University of Tartu - Естонія',

        ('Masaryk University', 'Чехія'):
            'Masaryk University, Чехія',
    }

    for program in ExchangeProgram.objects.all():
        key = (program.university, program.country)

        if key in data:
            program.university = data[key]
            program.country = ''

            program.save(
                update_fields=['university', 'country']
            )


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0006_exchangeprogram_country'),
    ]

    operations = [
        migrations.RunPython(
            split_university_country,
            restore_university_country,
        ),
    ]