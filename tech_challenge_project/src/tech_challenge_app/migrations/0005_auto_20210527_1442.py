# Generated by Django 3.2.3 on 2021-05-27 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech_challenge_app', '0004_auto_20210527_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='province',
            field=models.CharField(blank=True, help_text='province like ON, AB', max_length=2),
        ),
        migrations.AlterField(
            model_name='record',
            name='province',
            field=models.CharField(blank=True, help_text='province like ON, AB', max_length=2),
        ),
    ]
