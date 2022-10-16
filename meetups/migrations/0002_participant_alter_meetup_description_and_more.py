# Generated by Django 4.0.7 on 2022-10-15 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='meetup',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='meetup',
            name='participants',
            field=models.ManyToManyField(blank=True, null=True, to='meetups.participant'),
        ),
    ]
