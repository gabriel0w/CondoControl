from django.urls import path
from . import views

# URLConf
urlpatterns = [
	path('moradores/', views.moradores),
	path('prestadores/', views.prestadores),
	path('morador/<str:pk>/', views.morador)
]