from django.urls import path
from . import views

# URLConf
urlpatterns = [
	path('moradores/hello/', views.say_hello),
]