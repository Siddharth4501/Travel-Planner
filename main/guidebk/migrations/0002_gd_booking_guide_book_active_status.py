# Generated by Django 4.2.7 on 2023-12-03 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guidebk', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gd_booking',
            name='guide_book_active_status',
            field=models.BooleanField(default=False),
        ),
    ]
