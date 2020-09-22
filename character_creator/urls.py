from django.urls import path

from . import views

app_name = 'character'

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:character_id>/', views.sheet, name='sheet'),
	path('create/', views.create, name='create'),
]
	