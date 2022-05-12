from rest_framework import viewsets
from .serializers import client_serializer
from .models import client

class client_viewset(viewsets.ModelViewSet):
    queryset=client.objects.all()
    serializer_class=client_serializer