# Generated by Django 4.2.13 on 2024-06-06 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0012_character_age_character_description_novel_genre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portrait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('character', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assistant.character')),
            ],
        ),
    ]
