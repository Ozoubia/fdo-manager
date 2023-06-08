from django.urls import path
from . import views

urlpatterns = [
    # person
    path('getPerson/', views.getPerson),
    path('addPerson/', views.addPerson),
    path('persons/<int:person_id>/', views.updatePerson),
    path('persons/<int:person_id>/patch/', views.patchPerson),
    path('persons/<int:person_id>/delete/', views.deletePerson),

    # organisation
    path('addOrganization/', views.addOrganization),
    path('getOrganization/', views.getOrganization),
    path('organisation/<int:organisation_id>/', views.updateOrganisation),
    path('organisation/<int:organisation_id>/patch/', views.patchOrganisation),
    path('organisation/<int:organisation_id>/delete/', views.deleteOrganisation),

    # service
    path('getService/', views.getService),
    path('addService/', views.addService),
    path('service/<int:service_id>/', views.updateService),
    path('service/<int:service_id>/patch/', views.patchService),
    path('service/<int:service_id>/delete/', views.deleteService),

    # creative work
    path('getCreativeWork/', views.getCreativeWork),
    path('addCreativeWork/', views.addCreativeWork),
    path('creativework/<int:creativework_id>/', views.updateCreativeWork),
    path('creativework/<int:creativework_id>/patch/', views.patchCreativeWork),
    path('creativework/<int:creativework_id>/delete/', views.deleteCreativeWork),

    # web api
    path('getWebapi/', views.getWebAPI),
    path("addWebapi/", views.addWebAPI),
    path('webapi/<int:webapi_id>/', views.updateWebAPI),
    path('webapi/<int:webapi_id>/patch/', views.patchWebAPI),
    path('webapi/<int:webapi_id>/delete/', views.deleteWebAPI),

    # software applications
    path('getSoftwareApp/', views.getSoftwareApp),
    path("addSoftwareApp/", views.addSoftwareApp),
    path('softwareApp/<int:softwareapp_id>/', views.updateSoftwareApp),
    path('softwareApp/<int:softwareapp_id>/patch/', views.patchSoftwareApp),
    path('softwareApp/<int:softwareapp_id>/delete/', views.deleteSoftwareApp),

]

