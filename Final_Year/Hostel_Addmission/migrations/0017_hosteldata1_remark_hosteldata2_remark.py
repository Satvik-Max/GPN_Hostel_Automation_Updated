# Generated by Django 4.2.4 on 2023-09-30 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel_Addmission', '0016_lists_k'),
    ]

    operations = [
        migrations.AddField(
            model_name='hosteldata1',
            name='remark',
            field=models.CharField(default='NA', max_length=200),
        ),
        migrations.AddField(
            model_name='hosteldata2',
            name='remark',
            field=models.CharField(default='NA', max_length=200),
        ),
    ]
