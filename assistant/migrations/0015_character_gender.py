# Generated by Django 4.2.13 on 2024-06-06 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0014_portrait_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='gender',
            field=models.TextField(blank=True),
        ),
    ]