# Generated by Django 4.2.13 on 2024-06-06 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0013_portrait'),
    ]

    operations = [
        migrations.AddField(
            model_name='portrait',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
