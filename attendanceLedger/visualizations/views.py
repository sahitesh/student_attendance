from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from .db import GetTableData
from .models import FirstYearStudent, SecondYearStudent, ThirdYearStudent
from django.db.models import Avg, Max, Min, Sum

class Home(APIView):
    def get(self, request):
        first_header = [a.name for a in FirstYearStudent._meta.get_fields()]
        first_header = [a.replace('_',' ').title() for a in first_header]
        
        second_header = [a.name for a in SecondYearStudent._meta.get_fields()]
        second_header = [a.replace('_',' ').title() for a in second_header]

        third_header = [a.name for a in ThirdYearStudent._meta.get_fields()]
        third_header = [a.replace('_',' ').title() for a in third_header]

        return render(request, 'home.html', {'firstYear': FirstYearStudent.objects.all(), 'first_header':first_header, 'secondYear': SecondYearStudent.objects.all(), 'second_header':second_header, 'thirdYear': ThirdYearStudent.objects.all(), 'third_header':third_header})

class FirstYearTable(APIView):
    def get(self, request):
        first_header = [a.name for a in FirstYearStudent._meta.get_fields()]
        first_header = [a.replace('_',' ').title() for a in first_header]
        
        return render(request, 'firstYear.html', {'firstYear': FirstYearStudent.objects.all(), 'first_header':first_header})

class SecondYearTable(APIView):
    def get(self, request):
        second_header = [a.name for a in SecondYearStudent._meta.get_fields()]
        second_header = [a.replace('_',' ').title() for a in second_header]
        
        return render(request, 'secondYear.html', {'secondYear': SecondYearStudent.objects.all(), 'second_header':second_header})

class ThirdYearTable(APIView):
    def get(self, request):
        third_header = [a.name for a in ThirdYearStudent._meta.get_fields()]
        third_header = [a.replace('_',' ').title() for a in third_header]
        
        return render(request, 'thirdYear.html', {'thirdYear': ThirdYearStudent.objects.all(), 'third_header':third_header})

class GetTable(APIView):
    def get(self, request):
        print('Hello')

    def post(self, request):
        response = GetTableData(request.data)
        return response
        