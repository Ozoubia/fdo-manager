from django.urls import path
from . import views

urlpatterns = [
    path('getfdo/', views.getFDO),
    path('addfdo/', views.addFDO),
    path('addprofile/', views.addProfiles),
    path('getprofile/', views.getProfiles),
    path('getrecord/', views.getRecords),
    path('addrecord/', views.addRecords),
    path('addmetadata/', views.addMetaData),
    path('getmetadata/', views.getMetaData),
]