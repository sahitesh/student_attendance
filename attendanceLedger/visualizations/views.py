from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from .db import GetTableData
from .models import FirstYearStudent

class Home(APIView):
    def get(self, request):
        header = [a.name for a in FirstYearStudent._meta.get_fields()]
        header = [a.replace('_',' ').title() for a in header]
        
        return render(request, 'home.html', {'records': FirstYearStudent.objects.all(), 'header':header})

class GetTable(APIView):
    def get(self, request):
        print('Hello')

    def post(self, request):
        response = GetTableData(request.data)
        return response
        