# Generated by Django 2.2.7 on 2019-11-04 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("subscriptions", "0004_auto_20191104_1303")]

    operations = [
        migrations.AddField(
            model_name="video",
            name="subscription_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="subscriptions.Subscription",
            ),
            preserve_default=False,
        )
    ]
