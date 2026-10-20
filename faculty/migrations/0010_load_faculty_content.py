from django.db import migrations


def load_faculty_content(apps, schema_editor):
    Department = apps.get_model('faculty', 'Department')
    Teacher = apps.get_model('faculty', 'Teacher')
    Program = apps.get_model('faculty', 'Program')
    HomePage = apps.get_model('faculty', 'HomePage')

    HomePage.objects.get_or_create(
        title='Факультет природничих наук НаУКМА',
        defaults={
            'description': (
                'Факультет природничих наук Національного університету '
                '«Києво-Могилянська академія» здійснює підготовку студентів '
                'у галузі природничих наук. Навчання поєднує фундаментальну '
                'теоретичну підготовку, практичну роботу та сучасні наукові дослідження.'
            ),
            'contact_info': (
                'Національний університет «Києво-Могилянська академія», '
                'м. Київ, вул. Григорія Сковороди, 2'
            ),
        }
    )

    ecology, _ = Department.objects.get_or_create(name='Кафедра екології')
    chemistry, _ = Department.objects.get_or_create(name='Кафедра хімії')
    biology, _ = Department.objects.get_or_create(name='Кафедра біології')

    boychenko, _ = Teacher.objects.get_or_create(
        name='Бойченко Світлана Григорівна',
        defaults={
            'position': 'доцент',
            'degree': 'доктор географічних наук',
            'department': ecology,
        }
    )

    vakuliuk, _ = Teacher.objects.get_or_create(
        name='Вакулюк Поліна Василівна',
        defaults={
            'position': 'професор',
            'degree': 'доктор технічних наук',
            'department': chemistry,
        }
    )

    antoniuk, _ = Teacher.objects.get_or_create(
        name='Антонюк Максим Зиновійович',
        defaults={
            'position': 'професор',
            'degree': 'доктор біологічних наук',
            'department': biology,
        }
    )

    ecology.head = boychenko
    ecology.save(update_fields=['head'])

    chemistry.head = vakuliuk
    chemistry.save(update_fields=['head'])

    biology.head = antoniuk
    biology.save(update_fields=['head'])

    Program.objects.get_or_create(
        name='Екологія',
        defaults={
            'code': 'E2',
            'description': (
                'Бакалаврська програма «Екологія» готує фахівців у галузі '
                'екології, охорони довкілля та сталого природокористування.'
            ),
            'coordinator_name': 'Козак Олена Міланівна',
            'coordinator_contact': '+38(063) 809 93 56, o.kozak@ukma.edu.ua',
            'department': ecology,
            'disciplines': (
                'Екологія рослин з основами ботаніки\n'
                'Екологія тварин з основами зоології\n'
                'Аналітична хімія довкілля\n'
                'Органічна хімія з основами біохімії\n'
                'Моніторинг довкілля з основами метрології\n'
                'Екологічне право\n'
                'Техноекологія'
            ),
        }
    )

    Program.objects.get_or_create(
        name='Хімія',
        defaults={
            'code': 'E3',
            'description': (
                'Бакалаврська програма «Хімія» поєднує фундаментальну '
                'природничу підготовку з сучасними напрямами хімічної науки '
                'та практичними дослідженнями.'
            ),
            'coordinator_name': 'Вакулюк Поліна Василівна',
            'coordinator_contact': '+38(050) 611 78 42, vakuliuk@ukma.edu.ua',
            'department': chemistry,
            'disciplines': (
                'Вища математика\n'
                'Загальна хімія\n'
                'Неорганічна хімія\n'
                'Органічна хімія\n'
                'Аналітична хімія\n'
                'Фізична хімія\n'
                'Квантова хімія\n'
                'Хімія наноматеріалів'
            ),
        }
    )

    Program.objects.get_or_create(
        name='Біологія та біотехнологія',
        defaults={
            'code': 'E1',
            'description': (
                'Бакалаврська програма «Біологія та біотехнологія» поєднує '
                'фундаментальну біологічну підготовку з сучасними '
                'біотехнологічними підходами та дослідницькою практикою.'
            ),
            'coordinator_name': 'Антонюк Максим Зиновійович',
            'coordinator_contact': '+38(066)735 29 06, antonyuk.m@ukma.edu.ua',
            'department': biology,
            'disciplines': (
                'Цитологія та гістологія\n'
                'Ботаніка\n'
                'Біохімія\n'
                'Зоологія хордових\n'
                'Молекулярна біологія\n'
                'Імунологія\n'
                'Мікробіологія\n'
                'Молекулярні основи біотехнології'
            ),
        }
    )


def remove_faculty_content(apps, schema_editor):
    Program = apps.get_model('faculty', 'Program')
    Teacher = apps.get_model('faculty', 'Teacher')
    Department = apps.get_model('faculty', 'Department')
    HomePage = apps.get_model('faculty', 'HomePage')

    Program.objects.filter(
        name__in=[
            'Екологія',
            'Хімія',
            'Біологія та біотехнологія',
        ]
    ).delete()

    Department.objects.filter(
        name__in=[
            'Кафедра екології',
            'Кафедра хімії',
            'Кафедра біології',
        ]
    ).update(head=None)

    Teacher.objects.filter(
        name__in=[
            'Бойченко Світлана Григорівна',
            'Вакулюк Поліна Василівна',
            'Антонюк Максим Зиновійович',
        ]
    ).delete()

    Department.objects.filter(
        name__in=[
            'Кафедра екології',
            'Кафедра хімії',
            'Кафедра біології',
        ]
    ).delete()

    HomePage.objects.filter(
        title='Факультет природничих наук НаУКМА'
    ).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0009_alter_exchangeprogram_places'),
    ]

    operations = [
        migrations.RunPython(
            load_faculty_content,
            remove_faculty_content,
        ),
    ]
