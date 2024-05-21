# Generated by Django 4.2.13 on 2024-05-21 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assistant', '0004_paragraph_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('novel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assistant.novel')),
            ],
        ),
    ]