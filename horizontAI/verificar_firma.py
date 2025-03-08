import os
import sys
import django
import jwt
from django.conf import settings
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.exceptions import TokenError

# Configuración de Django
sys.path.append('C:\\Users\\USUARIO\\horizontAI')  # Ruta al proyecto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'horizontAI.settings')
django.setup()

# Nuevo token generado
token = "<eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQxNDMxODEzLCJpYXQiOjE3NDE0MjgyMTMsImp0aSI6IjJhYjBmNGJhNTA4OTRjMjRiNDc4YTVjMjFmNGQ5ZDVmIiwidXNlcl9pZCI6MSwiaXNzIjoiaHR0cDovLzEyNy4wLjAuMTo4MDAwLyJ9.MBaGpLSPrRzCcIvDIbnGEKRKC7T-T7ySGBUBRSh4ppo>"  # Reemplaza con el nuevo token
secret_key = settings.SECRET_KEY  # Obtiene la clave desde settings.py

header = jwt.get_unverified_header(token)
payload = jwt.decode(token, options={"verify_signature": False})
print("Encabezado:", header)
print("Payload:", payload)

# Validación manual con jwt.decode
print("\n[Validación manual con jwt.decode]")
try:
    decoded = jwt.decode(token, secret_key, algorithms=["HS256"])
    print("El token es válido. Datos decodificados:", decoded)
except jwt.ExpiredSignatureError:
    print("El token ha expirado. Genera uno nuevo.")
except jwt.InvalidSignatureError:
    print("La firma del token es inválida. Verifica tu SECRET_KEY.")
except jwt.InvalidTokenError as e:
    print(f"El token es inválido: {e}")

# Validación con AccessToken
print("\n[Validación con AccessToken]")
try:
    decoded = AccessToken(token)
    print("Token válido. Datos decodificados:", dict(decoded))
except TokenError as e:
    print("Error de token:", str(e))
