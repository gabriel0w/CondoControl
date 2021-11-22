from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

# URLConf
urlpatterns = [
	path('moradores/<str:apartamento>/', views.residentes),
	path('prestadores/', views.prestadores),
	path('morador/<str:pk>/', views.morador)
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)