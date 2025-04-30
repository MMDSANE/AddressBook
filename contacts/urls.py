from django.urls import path
from . import views

app_name = "landing"
urlpatterns = [
    path('contactlist/', views.contacts_list, name='contacts_list'),
    path('singlecontact/<int:id>', views.single_contact, name='single_contact'),

]