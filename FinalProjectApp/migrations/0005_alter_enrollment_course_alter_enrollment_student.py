# Generated by Django 4.2 on 2023-04-24 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("FinalProjectApp", "0004_enrollment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="enrollment",
            name="course",
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name="enrollment",
            name="student",
            field=models.CharField(max_length=100),
        ),
    ]
