from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from .db import GetTableData
from .models import FirstYearStudent

class Home(APIView):
    def get(self, request):
        return render(request, 'index.html', {'records': FirstYearStudent.objects.all()})

class GetTable(APIView):
    def get(self, request):
        print('Hello')

    def post(self, request):
        response = GetTableData(request.data)
        return response
        