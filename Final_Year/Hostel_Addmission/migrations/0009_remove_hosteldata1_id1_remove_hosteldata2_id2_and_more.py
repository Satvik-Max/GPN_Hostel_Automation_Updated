# Generated by Django 4.2.4 on 2023-08-21 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel_Addmission', '0008_hosteldata1_id_hosteldata2_id_hosteldata3_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hosteldata1',
            name='ID1',
        ),
        migrations.RemoveField(
            model_name='hosteldata2',
            name='ID2',
        ),
        migrations.RemoveField(
            model_name='hosteldata3',
            name='ID3',
        ),
    ]