# Generated by Django 3.2.7 on 2021-10-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0006_lead_call_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='initial_lead_date_time',
            field=models.DateTimeField(null=True),
        ),
    ]
