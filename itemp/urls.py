# from unicodedata import name
# from django import views
# from django.urls import path
# from.import views

# urlpatterns = [
#     path('index',views.index,name='index'),
#     path('custom_logout',views.custom_logout,name='custom_logout'),
#     path('admin_home',views.admin_home,name='admin_home'),
#     path('tl_home',views.tl_home,name='tl_home'),
#     path('dev_home',views.dev_home,name='dev_home'),
#     path('tl_signup',views.tl_signup,name='tl_signup'),
#     path('dev_signup',views.dev_signup,name='dev_signup'),
#     path('',views.login,name='login'),
#     path('loginaction',views.loginaction,name='loginaction'),
#     path('adddep',views.adddep,name='adddep'),
#     path('addproject',views.addproject,name='addproject'),
#     path('projectpublish',views.projectpublish,name='projectpublish'),
#     path('addcourse',views.addcourse,name='addcourse'),
#     path('devsignupaction',views.devsignupaction,name='devsignupaction'),
#     path('validatedev',views.validatedev,name='validatedev'),
#     path('tlsignupaction',views.tlsignupaction,name='tlsignupaction'),
#     path('approvedev/<str:username>',views.approvedev,name='approvedev'),
#     path('approvetl/<str:username>',views.approvetl,name='approvetl'),

#     path('reject/<str:username>',views.reject,name='reject'),
#     path('reject_dev/<str:username>',views.reject_dev,name='reject_dev'),
#     path('validatetl',views.validatetl,name='validatetl'),
#     path('changepassword',views.changepassword,name='changepassword'),
#     path('updatepassword',views.updatepassword,name='updatepassword'),
#     path('assignview',views.assignview,name='assignview'),
#     path('assignedtlview',views.assignedtlview,name='assignedtlview'),
#     path('progress',views.progress,name='progress'),
#     path('progress1',views.progress1,name='progress1'),
#     path('manage_users',views.manage_users,name='manage_users'),
#     path('assignmodule',views.assignmodule,name='assignmodule'),
#     path('adduser',views.adduser,name='adduser'),
#     path('deleteuser',views.deleteuser,name='deleteuser'),

#     path('promoteuser',views.promoteuser,name='promoteuser'),
#     path('moduleprogress',views.moduleprogress,name='moduleprogress'),
#     path('devprogress',views.devprogress,name='devprogress'),
#     path('tlprojects',views.tlprojects,name='tlprojects'),
#     path('tl_project_list',views.tl_project_list,name='tl_project_list'),
#     path('password_reset_confirm<str:username>',views.password_reset_confirm,name='password_reset_confirm'),
#     path('password_reset_request',views.password_reset_request,name='password_reset_request'),

    

#     path('modulefile/<int:id>',views.modulefile,name='modulefile'),

#     path('depromouser/<str:username>',views.depromouser,name='depromouser'),

#     path('promouser/<str:username>',views.promouser,name='promouser'),

#     path('deluser/<str:username>/<str:role>',views.deluser,name='deluser'),
    

    
#     path('progressupdate/<str:title>',views.progressupdate,name='progressupdate'),

#     path('download/<int:pdf_id>',views.download_pdf,name='download_pdf'),

#     path('download1/<int:pdf_id>',views.download_pdf1,name='download_pdf1'),
    
#     path('download2/<int:pdf_id>',views.download_pdf2,name='download_pdf2'),

#     path('progressupdate/progressupdate/<str:title>',views.progressupdate,name='progressupdate'),

#     path('editpage',views.editpage,name='editpage'),
#     path('edit_tl_details/<str:username>',views.edit_tl_details,name='edit_tl_details'),
#     path('editpage_dev',views.editpage_dev,name='editpage_dev'),
#     path('tl_profile',views.tl_profile,name='tl_profile'),
#     path('dev_profile',views.dev_profile,name='dev_profile'),
#     path('edit_dev_details/<str:username>',views.edit_dev_details,name='edit_dev_details'),

#     path('changepassword_dev',views.changepassword_dev,name='changepassword_dev'),
#     path('updatepassword_dev',views.updatepassword_dev,name='updatepassword_dev'),
    
    

# ]
from unicodedata import name
from django import views
from django.urls import path
from.import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('custom_logout',views.custom_logout,name='custom_logout'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('tl_home',views.tl_home,name='tl_home'),
    path('dev_home',views.dev_home,name='dev_home'),
    path('tl_signup',views.tl_signup,name='tl_signup'),
    path('dev_signup',views.dev_signup,name='dev_signup'),
    path('',views.login,name='login'),
    path('loginaction',views.loginaction,name='loginaction'),
    path('adddep',views.adddep,name='adddep'),
    path('addproject',views.addproject,name='addproject'),
    path('projectpublish',views.projectpublish,name='projectpublish'),
    path('addcourse',views.addcourse,name='addcourse'),
    path('devsignupaction',views.devsignupaction,name='devsignupaction'),
    path('validatedev',views.validatedev,name='validatedev'),
    path('tlsignupaction',views.tlsignupaction,name='tlsignupaction'),
    path('approvedev/<str:username>',views.approvedev,name='approvedev'),
    path('approvetl/<str:username>',views.approvetl,name='approvetl'),

    path('reject/<str:username>',views.reject,name='reject'),
    path('reject_dev/<str:username>',views.reject_dev,name='reject_dev'),
    path('validatetl',views.validatetl,name='validatetl'),
    path('changepassword',views.changepassword,name='changepassword'),
    path('updatepassword',views.updatepassword,name='updatepassword'),
    path('assignview',views.assignview,name='assignview'),
    path('assignedtlview',views.assignedtlview,name='assignedtlview'),
    path('progress',views.progress,name='progress'),
    path('progress1',views.progress1,name='progress1'),
    path('progress2',views.progress2,name='progress2'),
    path('manage_users',views.manage_users,name='manage_users'),
    path('assignmodule',views.assignmodule,name='assignmodule'),
    path('adduser',views.adduser,name='adduser'),
    path('deleteuser',views.deleteuser,name='deleteuser'),

    path('promoteuser',views.promoteuser,name='promoteuser'),
    path('moduleprogress',views.moduleprogress,name='moduleprogress'),
    path('devprogress',views.devprogress,name='devprogress'),
    path('tlprojects',views.tlprojects,name='tlprojects'),
    path('tl_project_list',views.tl_project_list,name='tl_project_list'),
    path('password_reset_confirm<str:username>',views.password_reset_confirm,name='password_reset_confirm'),
    path('password_reset_request',views.password_reset_request,name='password_reset_request'),

    

    path('modulefile/<int:id>',views.modulefile,name='modulefile'),

    path('depromouser/<str:username>',views.depromouser,name='depromouser'),

    path('promouser/<str:username>',views.promouser,name='promouser'),

    path('deluser/<str:username>/<str:role>',views.deluser,name='deluser'),
    

    
    path('progressupdate/<str:title>',views.progressupdate,name='progressupdate'),

    path('download/<int:pdf_id>',views.download_pdf,name='download_pdf'),

    path('download2/<int:pdf_id>',views.download_pdf2,name='download_pdf2'),

    path('download1/<int:pdf_id>',views.download_pdf1,name='download_pdf1'),
    
    path('download3/<int:pdf_id>',views.download_pdf3,name='download_pdf3'),

    path('progressupdate/progressupdate/<str:title>',views.progressupdate,name='progressupdate'),

    path('editpage',views.editpage,name='editpage'),
    path('edit_tl_details/<str:username>',views.edit_tl_details,name='edit_tl_details'),
    path('editpage_dev',views.editpage_dev,name='editpage_dev'),
    path('tl_profile',views.tl_profile,name='tl_profile'),
    path('dev_profile',views.dev_profile,name='dev_profile'),
    path('edit_dev_details/<str:username>',views.edit_dev_details,name='edit_dev_details'),

    path('changepassword_dev',views.changepassword_dev,name='changepassword_dev'),
    path('updatepassword_dev',views.updatepassword_dev,name='updatepassword_dev'),
    
    
    path('adminprogress',views.adminprogress,name='adminprogress'),
    path('p_progress',views.p_progress,name='p_progress'),
    path('projectprogress',views.projectprogress,name='projectprogress'),
    path('verify/<int:id>',views.verify,name='verify'),
    path('verify1/<int:id>',views.verify1,name='verify1'),
    path('verify2/<int:id>',views.verify2,name='verify2'),
    path('moredetails/<int:id>',views.moredetails,name='moredetails'),
    path('mark_completed/<str:project>',views.mark_completed,name='mark_completed'),

    path('mark_completed1/<str:project>',views.mark_completed1,name='mark_completed1'),
    path('mod_update',views.mod_update,name='mod_update'),
    path('modprogress',views.modprogress,name='modprogress'),
    path('moredetails1/<int:id>',views.moredetails1,name='moredetails1'),
    path('moredetails2/<int:id>',views.moredetails2,name='moredetails2'),




]
