# Generated by Django 5.1.4 on 2025-01-05 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_contact_delete_contactformsubmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobOpening',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('details_url', models.URLField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
