# Generated by Django 4.2.4 on 2023-08-24 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel_Addmission', '0011_alter_hosteldata1_branch_alter_hosteldata1_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='hosteldata1',
            name='fno1',
            field=models.IntegerField(default=1000),
        ),
        migrations.AddField(
            model_name='hosteldata2',
            name='fno2',
            field=models.IntegerField(default=2000),
        ),
        migrations.AddField(
            model_name='hosteldata3',
            name='fno3',
            field=models.IntegerField(default=3000),
        ),
    ]