from rest_framework import viewsets
from django.http import HttpResponse
from .models import Sociedade, Membro
from .serializers import SociedadeSerializer, MembroSerializer

# View simples para a página inicial
def home(request):
    return HttpResponse("<h1>Bem-vindo ao sistema de "
                        "gestão da igreja!</h1>")

# API para gerenciar sociedades
class SociedadeViewSet(viewsets.ModelViewSet):
    queryset = Sociedade.objects.all()
    serializer_class = SociedadeSerializer

# API para gerenciar membros
class MembroViewSet(viewsets.ModelViewSet):
    queryset = Membro.objects.all()
    serializer_class = MembroSerializer
