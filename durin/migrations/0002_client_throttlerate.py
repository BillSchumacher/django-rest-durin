# Generated by Django 3.2.3 on 2021-05-19 08:25

import datetime

from django.db import migrations, models

import durin.throttling


class Migration(migrations.Migration):

    dependencies = [
        ("durin", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="client",
            name="throttle_rate",
            field=models.CharField(
                blank=True,
                default="",
                help_text="Follows the same format as DRF's throttle rates.\n            Format: <em>'number_of_requests/period'</em>\n            where period should be one of: ('s', 'm', 'h', 'd').\n            Example: '100/h' implies 100 requests each hour.\n            ",
                max_length=64,
                validators=[
                    durin.throttling.UserClientRateThrottle.validate_client_throttle_rate
                ],
                verbose_name="Throttle rate for requests authed with this client",
            ),
        ),
        migrations.AlterField(
            model_name="authtoken",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="client",
            name="token_ttl",
            field=models.DurationField(
                default=datetime.timedelta(days=1),
                help_text="\n            Token Time To Live (TTL) in timedelta. Format: <code>DAYS HH:MM:SS</code>.\n            ",
                verbose_name="Token Time To Live (TTL)",
            ),
        ),
    ]