from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Product
from .serializers import ProductSerializer


# Create your views here.
def home(request):
    return render(request, 'index.html')


@csrf_exempt
def EcommerceAPI(request, id=0):
    if request.method == 'GET':
        products = Product.objects.all()
        ecommerce_serializers = ProductSerializer(products, many=True)
        return JsonResponse(ecommerce_serializers.data, safe=False)

    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        ecommerce_serializers = ProductSerializer(data=product_data)
        if ecommerce_serializers.is_valid():
            ecommerce_serializers.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)

    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)
        product = Product.objects.get(id=product_data['id'])
        ecommerce_serializers = ProductSerializer(product, data=product_data)
        if ecommerce_serializers.is_valid():
            ecommerce_serializers.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to update")

    elif request.method == 'DELETE':
        product = Product.objects.get(id=id)
        product.delete()
        return JsonResponse("Deleted Successfully", safe=False)
