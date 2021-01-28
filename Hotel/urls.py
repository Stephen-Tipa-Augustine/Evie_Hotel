from django.urls import path
from . import views

app_name = 'Hotel'
urlpatterns = [
    path('contact/', views.contact, name="contact"),
    path('booking/', views.book_table, name="booking"),
]