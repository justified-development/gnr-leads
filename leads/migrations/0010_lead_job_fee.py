# Generated by Django 3.2.7 on 2021-10-28 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0009_lead_won_job_date_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='job_fee',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
