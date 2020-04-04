from django.urls import path,include


from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('countries/',views.country,name='country'),
    path('hospitals/',views.hospitals,name='hospitals'),
    path('rescue/',views.Rescue,name='rescue'),
    path('guidlines/',views.guid,name='guid'),
    path('details/',views.details,name='detail'),
    path('emergency/',views.emergency,name = 'emergency'),
]