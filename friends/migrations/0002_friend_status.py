# Generated by Django 3.2.23 on 2023-12-24 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted')], default='accepted', max_length=10),
        ),
    ]
