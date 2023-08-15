#use view layer with function or class based views in Django
#Declare a class by extending the django.views.View class and define 
#get() and post() methods inside it to handle HTTP requests
#the url pattern connects the path to the class with the as_view() method

from django.views import View
class NewView(View):
    def get(self, request):
        #view logic will be placed here
        return HttpResponse('response')
    
    
#the urls.py is updated as below
from myapp.views import NewView
urlpatterns = [
    path('about/', NewView.as_view()),
]

#difference between Function View and Generic View
#Render the template as the HTTP response- the return value of the funciton

from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    template = loader.get_template("myapp/index.html")
    context={}
    return HttpResponse(template.render(context, request))

#the app package folder exists inside the project's outer container folder.

#in the myapp/urls.py , define the URL pattern

path('/', views.index, name='index')

#you can include the URL definitions of myapp in the projects URL configuration:

urlpatterns = [
    ...,
    path('myapp/', include('myapp.urls'))
]

#use a template class instead. Simply define a class extending it and set the
#template_name attribute

from django.views.generic.base import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
    
# the corresponding URL pattern should incorporate this:
path('/', IndexView(), name='index')

