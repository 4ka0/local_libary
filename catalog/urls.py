from django.urls import path
from . import views


'''
The path() below function also specifies a name parameter, which is a 
unique identifier for this particular URL mapping. You can use the 
name to dynamically create a URL that points to the resource that the 
mapper is designed to handle. For example, we can use the name parameter 
to link to our home page from any other page by adding the following link 
in a template: <a href="{% url 'index' %}">Home</a>
'''

urlpatterns = [
    path('', views.index, name='index'),
]