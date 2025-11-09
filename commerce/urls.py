from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name='index'),
    path('prashanth/', views.prashanth, name='indexpage'),
    path('addrecord/',views.addrecordpage,name="addrecordpage"),
    path('addrecord/addrecorddb/',views.addrecorddb,name="addrecorddb"),
    path('onlyrecord/', views.onlyrecords, name="onlyrecord"),
    path('displayrecord/',views.displayrecordpage,name="displayrecordpage"),
    path('updaterecord/<int:customer_id>/', views.updaterecordpage, name="updaterecordpage"),
    path('updaterecorddb/<int:customer_id>/', views.updaterecorddb, name="updaterecorddb"),
    path("deleterecord/<int:customer_id>/", views.deleterecordpage, name="deleterecordpage"),
    path("deleterecorddb/<int:customer_id>/", views.deleterecorddb, name="deleterecorddb"),
    path("searchrecord/", views.searchrecordpage, name="searchrecordpage")
]