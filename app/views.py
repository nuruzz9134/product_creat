from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .models import *
from .serializer import *



class ProductMainModelView(APIView):

    def post(self,request):
        serializer = ProductMainModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        products = ProductMainModel.objects.all()
        serializer = ProductMainModelSerializer(products, many=True)
        return Response(serializer.data)




class ProductColourModelView(APIView):

    def post(self,request):
        serializer = ProductColourModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        products = ProductColourModel.objects.all()
        serializer = ProductColourModelSerializer(products, many=True)
        return Response(serializer.data)


class ProductImageModelView(APIView):

    def post(self,request):
        serializer = ProductImageModellSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request):
        products = ProductImageModel.objects.all()
        serializer = ProductImageModellSerializer(products, many=True)
        return Response(serializer.data)




# get product detailed by id
class One_ProductDetailedView(APIView):

    def get(self,request):
        product_id = request.data['product_id']
        if ProductMainModel.objects.filter(id = product_id).exists():
            data =  ProductMainModel.objects.filter(id=product_id)

            all_data = []
            for i in data:
                print("iiiiiiii   : >>  ",i.__dict__)

                filtered_data ={}
                filtered_data = {
                                "Title":i.Title,
                                "description":i.description,
                                "Price":i.Price,
                                "size":i.size,
                                "Quality":i.Quality
                            }


                colour = ProductColourModel.objects.filter(id=product_id).first().Colour
                filtered_data['Colour'] = colour

                img = ProductImageModel.objects.filter(id=product_id).first().Image

                img_url = str(settings.MEDIA_ROOT)+"/"+ str(img)

                all_data.append(filtered_data)

            return Response([all_data,img_url])