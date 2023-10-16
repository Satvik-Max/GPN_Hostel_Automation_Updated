from django.urls import path 
from . import views
 
student_access = True

if student_access:
    urlpatterns = [
        path('',views.home,name='home'),
        path('Hostelview/',views.Hostellook,name='previewtab'),
        path('Admin_Login/',views.admin_log,name='admin_log'),
        path('logout/',views.logout,name='logout'),
        path('1stYear_Report/',views.Year1_report,name='report1'),
        path('3rdYear_Report/',views.Year3_report,name='report3'),
        path('2ndYear_Report/',views.Year2_report,name='report2'),
        path('Provisional_list3/',views.Provisional_list3,name='Provisional_list3'),
        path('Provisional_list2/',views.Provisional_list2,name='Provisional_list2'),
        path('Provisional_list1/',views.Provisional_list1,name='Provisional_list1'),

        path('search_student_3rdYear/',views.Search3,name='search3'),
        path('search_student_2ndYear/',views.Search2,name='search2'),
        path('search_student_1stYear/',views.Search1,name='search1'),

        path('Admin_Preview/<int:fno3>/',views.admin_Preview3,name='admin_preview3'),
        path('Admin_Preview2/<int:fno2>/',views.admin_Preview2,name='admin_preview2'),
        path('Admin_Preview1/<int:fno1>/',views.admin_Preview1,name='admin_preview1'),

        path('student_access',views.close_Forms,name='close_form'),
        path('student_access2',views.close_Forms2,name='close_form2'),
        path('student_access1',views.close_Forms1,name='close_form1'),

        path('First_year/',views.First_year,name='First_year'),
        path('Second_year/',views.Second_year,name='Second_year'),
        path('Third_year/',views.Third_year,name='Third_year'),
        path('Third_year_Mining/',views.Third_yearmining,name='Third_year_Mining'),
        path('Second_year_Mining/',views.Second_year_mining,name='Second_year_Mining'),

        path('Student_view/',views.student_Preview,name='S_view'),
        path('Student_view2/',views.student_Preview2,name='S_view2'),
        path('Student_view1/',views.student_Preview1,name='S_view1'),

        path('important_datea/',views.important_dates,name='imp_dates'),
        path('important_datea2/',views.important_dates2,name='imp_dates2'),
        path('important_datea1/',views.important_dates1,name='imp_dates1'),

        path('Up_Date/',views.up_date,name='up_date'),
        path('Up_Date2/',views.up_date2,name='up_date2'),
        path('Up_Date1/',views.up_date1,name='up_date1'),

        path('plist/',views.plistshow,name='plist'),
        path('flist/',views.flistshow,name='flist'),
        path('plist22/',views.plistshow22,name='plist22'),
        path('flist22/',views.flistshow22,name='flist22'),
        path('plist11/',views.plistshow11,name='plist11'),
        path('flist11/',views.flistshow11,name='flist11'),

        path('closeplist3/',views.closeplist,name='cplist3'),
        path('closeflist3/',views.closeflist,name='cflist3'),
        path('closeplist2/',views.closeplist2,name='cplist2'),
        path('closeflist2/',views.closeflist2,name='cflist2'),
        path('closeplist1/',views.closeplist1,name='cplist1'),
        path('closeflist1/',views.closeflist1,name='cflist1'),

        path('Addplist/',views.plistUP,name='addplist'),
        path('Addplist2/',views.plistUP2,name='addplist2'),
        path('Addplist1/',views.plistUP1,name='addplist1'),

        path('Addflist/',views.flistUP,name='addflist'),
        path('Addflist2/',views.flistUP2,name='addflist2'),
        path('Addflist1/',views.flistUP1,name='addflist1'),

        path('cimp3/',views.close_impdates3,name='cimp33'),
        path('cimp2/',views.close_impdates2,name='cimp22'),
        path('cimp1/',views.close_impdates1,name='cimp11'),
]