# Generated by Django 2.2.7 on 2019-11-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0006_auto_20191104_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='type',
            field=models.IntegerField(),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='youtube_id',
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
    ]
