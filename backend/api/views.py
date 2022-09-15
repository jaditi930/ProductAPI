from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer
from .models import Product
# Create your views here.
@api_view(["GET","POST"])
def api_home(request,*args,**kwargs):
    instance=Product.objects.all().order_by("?").first()
    data=ProductSerializer(instance).data
    return Response({f"{instance.id}":data})

@api_view(["GET","POST"])
def api_create(request,*args,**kwargs):
    serializer=ProductSerializer(data=request.data)
    if serializer.is_valid():
        instance=serializer.save()
        return Response(serializer.data)

