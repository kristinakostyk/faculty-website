from django.db import migrations


def normalize_places(apps, schema_editor):
    ExchangeProgram = apps.get_model('faculty', 'ExchangeProgram')

    data = {
        'Uniwersytet Warszawski': '5',
        'KU Leuven': '2',
        'Vilnius University': '4',
        'Uniwersytet Jagielloński': '3',
        'University of Tartu': '2',
        'Masaryk University': '1',
    }

    for university, places in data.items():
        ExchangeProgram.objects.filter(
            university=university
        ).update(places=places)


def restore_places(apps, schema_editor):
    ExchangeProgram = apps.get_model('faculty', 'ExchangeProgram')

    data = {
        'Uniwersytet Warszawski': '5',
        'KU Leuven': '2 місця',
        'Vilnius University': 'до 4',
        'Uniwersytet Jagielloński': '3',
        'University of Tartu': '2',
        'Masaryk University': '1 місце',
    }

    for university, places in data.items():
        ExchangeProgram.objects.filter(
            university=university
        ).update(places=places)


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0007_split_university_country'),
    ]

    operations = [
        migrations.RunPython(
            normalize_places,
            restore_places,
        ),
    ]