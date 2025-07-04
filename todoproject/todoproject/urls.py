
from django.contrib import admin
from django.urls import path
from todoApp.views import*

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registerpage/',registerpage,name='registerpage'),
    path('',loginpage,name='loginpage'),
    path('homepage/',homepage,name='homepage'),
    path('logoutpage/',logoutpage,name='logoutpage'),
    path('changepassword/',changepassword,name='changepassword'),
    path('tasklist/',tasklist,name='tasklist'),
    path('addtask/',addtask,name='addtask'),
    path('editpage/<str:id>',editpage,name='editpage'),
    path('viewpage/<str:id>',viewpage,name='viewpage'),
    path('deletepage/<str:id>',deletepage,name='deletepage'),
]
