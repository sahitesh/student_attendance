from rest_framework.views import APIView
from django.shortcuts import render
from django.http import HttpResponse
from .db import GetTableData
from .models import FirstYearStudent, SecondYearStudent, ThirdYearStudent, SampleStatistics
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

class ThirdYearStatistics(APIView):
    def get(self, request):
        subjects = SampleStatistics.objects.all()
        table_statistics = []
        dict_object = {}
        total_classes = {}
        
        for subject in subjects:
            dict_object['Subject'] = subject.subject_id
            
            print(dict_object)
            total_classes['{}'.format(subject.subject_id)] = subject.total_classes
            


        third_header = ["Subject", "Total Number of Students","Students Passed","Students attendance(>75%)","Students Passed(>75%)", "Students attandance(65% to 75%)","Students Passed(65% to 75%)","Students Attendance(<65%)","Students Passed(<65%)"]
        sectiona_students = ThirdYearStudent.objects.all().filter(section_id = 'A')
        for subject in total_classes.keys():
            table_statistics_temp = []
            kwargs_common = {
                '{}_points__gt'.format(subject) : 0 
            }
            kwargs = {
                '{}_points__gt'.format(subject): 0
            }
            table_statistics_temp.append(subject.upper())
            table_statistics_temp.append(len(sectiona_students))
            table_statistics_temp.append(len(sectiona_students.filter(**kwargs)))
            kwargs = {
                '{}_attendance__gt'.format(subject): 0.75*total_classes[subject]
            }
            attendance_75 = sectiona_students.filter(**kwargs)
            table_statistics_temp.append(len(attendance_75))
            table_statistics_temp.append(len(attendance_75.filter(**kwargs_common)))
            kwargs = {
                '{}_attendance__lte'.format(subject) : 0.75*total_classes[subject],
                '{}_attendance__gt'.format(subject) : 0.65*total_classes[subject]
            }
            attendance_65_75 = sectiona_students.filter(**kwargs)
            table_statistics_temp.append(len(attendance_65_75))
            table_statistics_temp.append(len(attendance_65_75.filter(**kwargs_common)))
            kwargs = {
                '{}_attendance__lte'.format(subject): 0.65*total_classes[subject]
            }
            attendance_65 = sectiona_students.filter(**kwargs)
            table_statistics_temp.append(len(attendance_65))
            table_statistics_temp.append(len(attendance_65.filter(**kwargs_common)))
            table_statistics.append(table_statistics_temp)


        return render(request, 'thirdYearStatistics.html', {'thirdYear': table_statistics, 'third_header':third_header})

class GetTable(APIView):
    def get(self, request):
        print('Hello')

    def post(self, request):
        response = GetTableData(request.data)
        return response
        