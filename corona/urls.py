from django.urls import path,include


from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('countries/',views.country,name='country'),
    path('hospitals/',views.hospitals,name='hospitals'),
]