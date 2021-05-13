# Generated by Django 3.2 on 2021-05-13 09:58

from django.db import migrations
import django.utils.timezone
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
