from django.urls import path

from . import views

app_name = 'character'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('<int:pk>/', views.play, name='play'),
	path('<int:pk>/sheet', views.DetailView.as_view(), name='sheet'),
	path('create/', views.create, name='create'),
	path('<int:pk>/roll/', views.roll, name='roll')
]
	