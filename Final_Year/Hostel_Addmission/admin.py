from django.contrib import admin
from .models import HostelData1
from .models import HostelData2
from .models import HostelData3
from .models import Lists

@admin.register(HostelData1)
class HostelDataAdmin(admin.ModelAdmin):
    list_display = ('name' ,  'Email' )


@admin.register(HostelData2)
class HostelDataAdmin(admin.ModelAdmin):
    list_display = ('name' ,  'Email' )


@admin.register(HostelData3)
class HostelDataAdmin(admin.ModelAdmin):
    list_display = ('name' ,  'Email' )


@admin.register(Lists)
class HostelDataAdmin(admin.ModelAdmin):
    list_display = ("k",)