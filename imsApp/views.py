from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

# Create your views here.

class CategoryAPI(APIView):
    #Retrieve
    def get(self, request):
        qs = Category.objects.all()
        ser = CategorySerializer(qs, many=True)
        return Response(ser.data)

    #Create
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Update
    def put(self, request):
        id = request.POST.get("id")        
        category = request.POST.get("category")        
        try:
            qs = Category.objects.get(id=id)
            if qs:
                qs.category = category
                qs.save()
                resp = {
                    'success' : 'true',
                    'message' : "Category Has Been Successfully Updated",
                }
                return Response(resp, status=status.HTTP_201_CREATED)
        except:       
            resp = {
                'success' : 'false',
                'message' : "Something went wrong try again",      
                }    
            return Response(resp, status=status.HTTP_304_NOT_MODIFIED) 
    #Delete
    def delete(self, request):
        id = request.POST.get("id")  
        try:           
            qs = Category.objects.get(id=id).delete()
            if qs:
                resp = {
                    'success' : 'true',
                    'message' : "Category Deleted",
                }
                return Response(resp, status=status.HTTP_200_OK)
        except:
            resp = {
                'success' : 'false',
                'message' : "Record does not exist",        }    
            return Response(resp, status=status.HTTP_400_BAD_REQUEST) 



class ProductAPI(APIView):
    #Retrieve Product    
    def get(self, request):
        qs = Product.objects.all()
        ser = ProductSerializer(qs, many=True)
        return Response(ser.data)

    #Create Product
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    #Update Product
    def put(self, request):
        id = request.POST.get("id")       
        product_name = request.POST.get("product_name")
        product_model_name = request.POST.get("product_model_name")
        price = request.POST.get("price")    
        try: 
            qs = Product.objects.get(id=id)
            if qs:
                qs.product_name = product_name
                qs.product_model_name = product_model_name
                qs.price = price
                qs.save()
                resp = {
                    'success' : 'true',
                    'message' : "Product Has Been Successfully Updated",
                }
                return Response(resp, status=status.HTTP_201_CREATED)
        except:
            resp = {
                'success' : 'false',
                'message' : "Something went wrong try again",      
                }    
            return Response(resp, status=status.HTTP_304_NOT_MODIFIED) 

    #Delete Product
    def delete(self, request):
        id = request.POST.get("id")  
        try:           
            qs = Product.objects.get(id=id).delete()
            if qs:
                resp = {
                    'success' : 'true',
                    'message' : "Product Deleted",
                }
                return Response(resp, status=status.HTTP_200_OK)
        except:
            resp = {
                'success' : 'false',
                'message' : "Record does not exist",        }    
            return Response(resp, status=status.HTTP_400_BAD_REQUEST) 