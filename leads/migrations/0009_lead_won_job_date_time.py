# Generated by Django 3.2.7 on 2021-10-28 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0008_rename_password_account_account_pass'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='won_job_date_time',
            field=models.DateTimeField(null=True),
        ),
    ]
