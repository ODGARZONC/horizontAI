from django.urls import path
from . import views  # Importa tus vistas desde el archivo views.py
from .views import AprobacionListCreate
from .views import ProtectedView
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import NotificacionesView

urlpatterns = [
    path('', views.index, name='index'),  # Ruta principal
    #path('', views.home, name='home'),  # Ruta para la página de inicio
    path('api/aprobaciones/', AprobacionListCreate.as_view(), name='aprobaciones'),
    path('protected/', ProtectedView.as_view(), name='protected_view'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/notificaciones/', NotificacionesView.as_view(), name='notificaciones')

]

