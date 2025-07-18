# Generated by Django 5.1.4 on 2025-06-21 22:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0006_rename_marks_subjectmarks_marks_reportcard'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportcard',
            name='date_of_report_card_generation',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='reportcard',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vege.student'),
        ),
        migrations.AlterUniqueTogether(
            name='reportcard',
            unique_together={('student_rank', 'date_of_report_card_generation')},
        ),
    ]
