from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from book import serializers
from book.models import Book





class SelectBooksView(APIView):
    def get(self,request):
        data=Book.objects.all().order_by('id')
        serializer=serializers.BookSerializer(data,context={"request":request}, many=True)
        return Response(serializer.data)
class AddBookView(APIView):
    def post(self,request):
        serializer=serializers.Book(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
            return Response(serializer.errors)

