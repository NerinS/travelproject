# from django.contrib import admin

from . import views
from django.urls import path,include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.demo,name='demo'),
    # path('',views.home,name='home'),
    # path('contact/',views.contact,name='contact'),
    # path('about/',views.about,name='about'),
    # path('details/',views.details,name='details'),
    # path('thanks/',views.thanks,name='thanks'),
    # path('add/',views.addition, name='addition')
]