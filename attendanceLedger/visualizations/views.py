from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from .db import GetTableData

class Home(APIView):
    def get(self, request):
        return render(request, 'home.html')

class GetTable(APIView):
    def get(self, request):
        print('Hello')

    def post(self, request):
        response = GetTableData(request.data)
        return response