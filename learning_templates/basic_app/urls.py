from django.urls import path
from . import views

# SET THE NAMESPACE - acts like a template tagging,  whenever we have a global variable, django goes there and checks the URL tha matches
app_name = 'basic_app'


urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),         
]
