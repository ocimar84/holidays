# Generated by Django 4.2 on 2023-04-18 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('holidays', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeoff',
            name='reason_text',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AddField(
            model_name='timeoff',
            name='status_text',
            field=models.CharField(default='pending', max_length=200),
        ),
    ]
