# Generated by Django 3.2.2 on 2021-05-16 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0002_rename_customers_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=64)),
                ('saccno', models.CharField(max_length=64)),
                ('rname', models.CharField(max_length=64)),
                ('raccno', models.CharField(max_length=64)),
                ('amnt', models.FloatField()),
            ],
        ),
    ]
