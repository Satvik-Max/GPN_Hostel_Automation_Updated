# Generated by Django 4.2.4 on 2023-08-09 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HostelData1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('cast', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=10)),
                ('BGroup', models.CharField(max_length=4)),
                ('phone1', models.IntegerField()),
                ('Address1', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=20)),
                ('Branch', models.CharField(max_length=20)),
                ('percentage', models.IntegerField()),
                ('Father_name', models.CharField(max_length=100)),
                ('phone2', models.IntegerField()),
                ('Address2', models.CharField(max_length=50)),
                ('student_signature', models.FileField(default='file.jpg', upload_to='signatures/student/')),
                ('father_signature', models.FileField(default='file.jpg', upload_to='signatures/father/')),
                ('marksheet', models.FileField(default='file.pdf', upload_to='marksheet/')),
                ('Domacile', models.FileField(default='file.pdf', upload_to='Domacile/')),
                ('Allotment', models.FileField(default='file.pdf', upload_to='Allotment/')),
                ('Addmission', models.FileField(default='file.pdf', upload_to='Addmission/')),
                ('Registration', models.FileField(default='file.pdf', upload_to='Registration/')),
            ],
        ),
        migrations.CreateModel(
            name='HostelData2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('cast', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=10)),
                ('BGroup', models.CharField(max_length=4)),
                ('phone1', models.IntegerField()),
                ('Address1', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=20)),
                ('Branch', models.CharField(max_length=20)),
                ('percentage', models.IntegerField()),
                ('Father_name', models.CharField(max_length=100)),
                ('phone2', models.IntegerField()),
                ('Address2', models.CharField(max_length=50)),
                ('student_signature', models.FileField(default='file.jpg', upload_to='2signatures/student/')),
                ('father_signature', models.FileField(default='file.jpg', upload_to='2signatures/father/')),
                ('marksheet1', models.FileField(default='file.pdf', upload_to='2marksheet1/')),
                ('marksheet2', models.FileField(default='file.pdf', upload_to='2marksheet2/')),
                ('Domacile', models.FileField(default='file.pdf', upload_to='2Domacile/')),
                ('Allotment', models.FileField(default='file.pdf', upload_to='2Allotment/')),
                ('Addmission', models.FileField(default='file.pdf', upload_to='2Addmission/')),
                ('Registration', models.FileField(default='file.pdf', upload_to='2Registration/')),
            ],
        ),
        migrations.CreateModel(
            name='HostelData3',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('DOB', models.DateField()),
                ('cast', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=10)),
                ('BGroup', models.CharField(max_length=4)),
                ('phone1', models.IntegerField()),
                ('Address1', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=20)),
                ('Branch', models.CharField(max_length=20)),
                ('percentage', models.IntegerField()),
                ('Father_name', models.CharField(max_length=100)),
                ('phone2', models.IntegerField()),
                ('Address2', models.CharField(max_length=50)),
                ('student_signature', models.FileField(default='file.jpg', upload_to='3signatures/student/')),
                ('father_signature', models.FileField(default='file.jpg', upload_to='3signatures/father/')),
                ('marksheet1', models.FileField(default='file.pdf', upload_to='3marksheet1/')),
                ('marksheet2', models.FileField(default='file.pdf', upload_to='3marksheet2/')),
                ('Domacile', models.FileField(default='file.pdf', upload_to='3Domacile/')),
                ('Allotment', models.FileField(default='file.pdf', upload_to='3Allotment/')),
                ('Addmission', models.FileField(default='file.pdf', upload_to='3Addmission/')),
                ('Registration', models.FileField(default='file.pdf', upload_to='3Registration/')),
            ],
        ),
    ]
