# Generated by Django 4.0.3 on 2023-09-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_goldprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='InputList1',
            fields=[
                ('title', models.TextField(blank=True, primary_key=True, serialize=False)),
                ('jobname', models.TextField(blank=True, null=True)),
                ('emblem', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'input_list1',
                'managed': False,
            },
        ),
    ]
