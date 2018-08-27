from django.conf.urls import url

from .views import Home, FirstYearTable, SecondYearTable, ThirdYearTable, ThirdYearStatistics

urlpatterns = [
    url(r'^$', Home.as_view(), name = 'homepage'),
    url('first', FirstYearTable.as_view(), name = 'firstyear'),
    url('second', SecondYearTable.as_view(), name = 'secondyear'),
    url('third', ThirdYearTable.as_view(), name = 'thirdyear'),
    url('statistics', ThirdYearStatistics.as_view(), name = 'thirdyearstatistics'),
]
