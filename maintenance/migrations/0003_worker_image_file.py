# Generated by Django 4.2.11 on 2024-05-20 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maintenance", "0002_alter_department_options_position_duties"),
    ]

    operations = [
        migrations.AddField(
            model_name="worker",
            name="image_file",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
