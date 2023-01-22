from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name = 'home'),
    path('list', views.divaHunkList, name='list'),
    path('diva/register/<int:pk>', views.divaRegistration, name='diva register'),
    path('hunk/register/<int:pk>/', views.hunkRegistration, name='hunk register'),
    path('thanks_diva',views.thanksdiva, name='thanks_diva'),       
    path('thanks_hunk',views.thankshunk, name='thanks_hunk')
]