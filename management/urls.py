from django.urls import path
from . import views

app_name = "management"
urlpatterns = [
    path('login/', views.login, name='login'),
    path('manage/', views.manage, name='manage'),
    path('manage/<int:contact_id>/', views.delete_contact, name='delete_contact'),
    path('manage/edit/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    # path('add/', views.add_contact, name='add_contact'),
]


