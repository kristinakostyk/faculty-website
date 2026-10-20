from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0004_exchangeprogram'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                INSERT INTO faculty_exchangeprogram
                (university, languages, places, deadline, description)
                VALUES
                (
                    'Uniwersytet Warszawski, Польща',
                    'польська, англійська',
                    '5',
                    '2026-11-15',
                    'Програма академічного обміну у Варшавському університеті дає можливість навчатися в міжнародному середовищі та обирати курси відповідно до напряму підготовки.'
                ),
                (
                    'KU Leuven (Бельгія)',
                    'English',
                    '2 місця',
                    '2026-12-01',
                    'Програма обміну в KU Leuven дозволяє студентам отримати міжнародний академічний досвід та навчатися в одному з провідних університетів Бельгії.'
                ),
                (
                    'Vilnius University, Литва',
                    'англійська',
                    'до 4',
                    '2026-10-20',
                    'Програма у Vilnius University пропонує навчання англійською мовою та можливість познайомитися з академічним середовищем Литви.'
                ),
                (
                    'Uniwersytet Jagielloński, Польща',
                    'Польська, Англійська',
                    '3',
                    '2026-11-15',
                    'Програма обміну в Ягеллонському університеті дає змогу пройти частину навчання в Польщі та долучитися до міжнародної студентської спільноти.'
                ),
                (
                    'University of Tartu - Естонія',
                    'англійська, естонська',
                    '2',
                    '2027-01-10',
                    'University of Tartu пропонує студентам міжнародний досвід навчання та широкий вибір академічних дисциплін.'
                ),
                (
                    'Masaryk University, Чехія',
                    'англійська',
                    '1 місце',
                    '2026-09-30',
                    'Програма академічного обміну в Masaryk University дозволяє навчатися англійською мовою та отримати досвід навчання у Чехії.'
                );
            """,
            reverse_sql="""
                DELETE FROM faculty_exchangeprogram
                WHERE university IN (
                    'Uniwersytet Warszawski, Польща',
                    'KU Leuven (Бельгія)',
                    'Vilnius University, Литва',
                    'Uniwersytet Jagielloński, Польща',
                    'University of Tartu - Естонія',
                    'Masaryk University, Чехія'
                );
            """
        ),
    ]