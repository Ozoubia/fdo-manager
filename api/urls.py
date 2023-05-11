from django.urls import path
from . import views

urlpatterns = [
    # person
    path('getPerson/', views.getPerson),
    path('addPerson/', views.addPerson),
    # organisation
    path('addOrganization/', views.addOrganization),
    path('getOrganization/', views.getOrganization),
    # service
    path('getService/', views.getService),
    path('addService/', views.addService),
    # creative work
    path('getCreativeWork/', views.getCreativeWork),
    path('addCreativeWork/', views.addCreativeWork),
    # web api
    path('getWebapi/', views.getWebAPI),
    path("addWebapi/", views.addWebAPI),
    # software applications
    path('getSoftwareApp/', views.getSoftwareApp),
    path("addSoftwareApp/", views.addSoftwareApp),

]

# urlpatterns = [
#     # fdo
#     path('getfdo/', views.getFDO),
#     path('addfdo/', views.addFDO),
#
#     # profile
#     path('addprofile/', views.addProfiles),
#     path('getprofile/', views.getProfiles),
#     path("getprofile/<int:id>/", views.getProfile),
#     path('updateprofile/<int:id>/', views.updateProfiles),
#     path('deleteprofile/<int:id>/', views.deleteProfile),
#
#     # records
#     path('getrecord/', views.getRecords),
#     path('addrecord/', views.addRecords),
#
#     # meta data
#     path('addmetadata/', views.addMetaData),
#     path('getmetadata/', views.getMetaData),
#
#     # artifact properties
#     path('addartprop/', views.addArtprop),
#     path('getartprop', views.getArtprop),
#
# ]