from django.contrib import admin
from .models import HostelData1
from .models import HostelData2
from .models import HostelData3
from .models import Lists

@admin.register(HostelData1)
class HostelDataAdmin(admin.ModelAdmin):
    list_display = ('fno1','name' ,  'Email' ,'phone1' )


@admin.register(HostelData2)
class HostelDataAdmin(admin.ModelAdmin):
    list_display = ('fno2','name' ,  'Email' ,'phone1' )


@admin.register(HostelData3)
class HostelDataAdmin(admin.ModelAdmin):
    list_display = ('fno3','name' ,  'Email' ,'phone1' )


@admin.register(Lists)
class HostelDataAdmin(admin.ModelAdmin):
    list_display = ("k",)


    # street1 = models.CharField(max_length=50)
    # city1 = models.CharField(max_length=50)
    # state1 = models.CharField(max_length=50)
    # pincode1 = models.CharField(max_length=50)
    # street2 = models.CharField(max_length=50)
    # city2 = models.CharField(max_length=50)
    # state2 = models.CharField(max_length=50)
    # pincode2 = models.CharField(max_length=50)