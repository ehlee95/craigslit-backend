# Generated by Django 4.0.4 on 2022-05-18 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craigslitapp', '0002_post_condition_post_location_post_notes_post_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='listingtype',
            field=models.CharField(default='', max_length=128),
        ),
    ]
