from django.urls import path 
from . import views 



app_name = 'folio'

urlpatterns = [
    path('' , views.home , name='home'),
]
