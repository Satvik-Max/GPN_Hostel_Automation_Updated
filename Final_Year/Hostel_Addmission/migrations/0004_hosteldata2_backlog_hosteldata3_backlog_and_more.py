# Generated by Django 4.2.4 on 2023-08-14 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hostel_Addmission', '0003_delete_adminlogin'),
    ]

    operations = [
        migrations.AddField(
            model_name='hosteldata2',
            name='Backlog',
            field=models.CharField(default='YES', max_length=3),
        ),
        migrations.AddField(
            model_name='hosteldata3',
            name='Backlog',
            field=models.CharField(default='YES', max_length=3),
        ),
        migrations.AlterField(
            model_name='hosteldata3',
            name='Branch',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='hosteldata3',
            name='Email',
            field=models.EmailField(max_length=50),
        ),
    ]
