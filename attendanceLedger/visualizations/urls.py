from django.conf.urls import url

from .views import Home, GetTable

urlpatterns = [
    url('', Home.as_view(), name = 'homepage'),
    url('tables', GetTable.as_view(), name = 'tables')
    
]
