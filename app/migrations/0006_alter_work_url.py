# Generated by Django 4.2.11 on 2024-06-03 01:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0005_software_technical"),
    ]

    operations = [
        migrations.AlterField(
            model_name="work",
            name="url",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="URL2"
            ),
        ),
    ]