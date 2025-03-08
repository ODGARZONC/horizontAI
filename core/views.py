from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Aprobacion
from .serializers import AprobacionSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse

def home(request):
    return HttpResponse("<h1>¡Bienvenido a HorizontAI!</h1>")

def index(request):
    return render(request, 'frontend/build/index.html')

class AprobacionListCreate(APIView):
    def get(self, request):
        aprobaciones = Aprobacion.objects.filter(estado='pendiente')
        serializer = AprobacionSerializer(aprobaciones, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AprobacionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProtectedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": "¡Vista protegida exitosa!"})
    
class NotificacionesView(APIView):
    def get(self, request):
        # Supongamos que se tiene un modelo Notificacion
        data = [
            {"id": 1, "mensaje": "Nueva solicitud de aprobación"},
            {"id": 2, "mensaje": "Pago pendiente por revisar"},
        ]
        return JsonResponse(data, safe=False)