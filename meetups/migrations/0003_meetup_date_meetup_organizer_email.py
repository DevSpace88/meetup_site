# Generated by Django 4.0.7 on 2022-10-15 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_participant_alter_meetup_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='date',
            field=models.DateField(default='2021-04-12'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meetup',
            name='organizer_email',
            field=models.EmailField(default='test@test.com', max_length=254),
            preserve_default=False,
        ),
    ]
