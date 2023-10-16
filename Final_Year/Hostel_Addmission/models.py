from django.db import models


class HostelData1(models.Model):

    fno1 = models.IntegerField(default=1000)
    name = models.CharField(max_length=100)
    DOB = models.DateField()
    cast = models.CharField(max_length=50)
    nationality = models.CharField(max_length=10)
    BGroup = models.CharField(max_length=4)
    phone1 = models.IntegerField()
    Address1 = models.CharField(max_length=50)
    Email = models.EmailField(max_length=30)

    Branch = models.CharField(max_length=30)
    percentage = models.IntegerField()

    Father_name = models.CharField(max_length=100)
    phone2 = models.IntegerField()
    Address2 = models.CharField(max_length=50)
    
    student_signature = models.FileField(upload_to='signatures/student/',default='file.jpg')
    father_signature = models.FileField(upload_to='signatures/father/',default='file.jpg')
    marksheet = models.FileField(upload_to='marksheet/', default='file.pdf')
    Domacile = models.FileField(upload_to='Domacile/', default='file.pdf')
    Allotment = models.FileField(upload_to='Allotment/', default='file.pdf')
    Addmission = models.FileField(upload_to='Addmission/', default='file.pdf')
    Registration  = models.FileField(upload_to='Registration/', default='file.pdf')

    remark = models.CharField(max_length=200, default='NA')

class HostelData2(models.Model):

    fno2 = models.IntegerField(default=2000)
    name = models.CharField(max_length=100)
    DOB = models.DateField()
    cast = models.CharField(max_length=50)
    nationality = models.CharField(max_length=10)
    BGroup = models.CharField(max_length=4)
    phone1 = models.IntegerField()
    Address1 = models.CharField(max_length=50)
    Email = models.EmailField(max_length=30)

    Branch = models.CharField(max_length=30)
    Backlog = models.CharField(max_length=3,default='YES')
    Nu_Backlog = models.IntegerField(default=0)
    percentage = models.IntegerField()

    Father_name = models.CharField(max_length=100)
    phone2 = models.IntegerField()
    Address2 = models.CharField(max_length=50)
    
    student_signature = models.FileField(upload_to='2signatures/student/',default='file.jpg')
    father_signature = models.FileField(upload_to='2signatures/father/',default='file.jpg')
    marksheet1 = models.FileField(upload_to='2marksheet1/', default='file.pdf')
    marksheet2 = models.FileField(upload_to='2marksheet2/', default='file.pdf')
    Domacile = models.FileField(upload_to='2Domacile/', default='file.pdf')
    Allotment = models.FileField(upload_to='2Allotment/', default='file.pdf')
    Addmission = models.FileField(upload_to='2Addmission/', default='file.pdf')
    Registration  = models.FileField(upload_to='2Registration/', default='file.pdf')

    remark = models.CharField(max_length=200, default='NA')

class HostelData3(models.Model):

    fno3 = models.IntegerField(default=3000)
    name = models.CharField(max_length=100)
    DOB = models.DateField()
    cast = models.CharField(max_length=50)
    nationality = models.CharField(max_length=10)
    BGroup = models.CharField(max_length=4)
    phone1 = models.IntegerField()
    Address1 = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)

    Branch = models.CharField(max_length=30)
    Backlog = models.CharField(max_length=3,default='YES')
    Nu_Backlog = models.IntegerField(default=0)
    percentage = models.IntegerField()

    Father_name = models.CharField(max_length=100)
    phone2 = models.IntegerField()
    Address2 = models.CharField(max_length=50)
  
    student_signature = models.FileField(upload_to='3signatures/student/',default='file.jpg')
    father_signature = models.FileField(upload_to='3signatures/father/',default='file.jpg')
    marksheet1 = models.FileField(upload_to='3marksheet1/', default='file.pdf')
    marksheet2 = models.FileField(upload_to='3marksheet2/', default='file.pdf')
    Domacile = models.FileField(upload_to='3Domacile/', default='file.pdf')
    Allotment = models.FileField(upload_to='3Allotment/', default='file.pdf')
    Addmission = models.FileField(upload_to='3Addmission/', default='file.pdf')
    Registration  = models.FileField(upload_to='3Registration/', default='file.pdf')

    remark = models.CharField(max_length=200, default='NA')


class Lists(models.Model):
    
    k = models.IntegerField(default=101010)
    p3 = models.FileField(upload_to='lists/', default='file.pdf')
    f3 = models.FileField(upload_to='lists/', default='file.pdf')
    p2 = models.FileField(upload_to='lists/', default='file.pdf')
    f2 = models.FileField(upload_to='lists/', default='file.pdf')
    p1 = models.FileField(upload_to='lists/', default='file.pdf')
    f1 = models.FileField(upload_to='lists/', default='file.pdf')