# Generated by Django 4.2.4 on 2023-08-21 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel_Addmission', '0007_hosteldata2_nu_backlog_hosteldata3_nu_backlog'),
    ]

    operations = [
        migrations.AddField(
            model_name='hosteldata1',
            name='ID1',
            field=models.CharField(default=1000, max_length=5),
        ),
        migrations.AddField(
            model_name='hosteldata2',
            name='ID2',
            field=models.CharField(default=2000, max_length=5),
        ),
        migrations.AddField(
            model_name='hosteldata3',
            name='ID3',
            field=models.CharField(default=3000, max_length=5),
        ),
    ]
