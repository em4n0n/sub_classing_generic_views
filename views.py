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

#requirements of a generic view

# if the vie neews a model to be processed, it should be set as the value
#model property of the view

#each type of view looks for a template name with modelname suffixed
#by the type of generic view. For example, for a list view of processing
#employee model, Django tries to find employee_list.html

# the generic view is mapped with the URL with as_view() method of the View class

#build a subclass for each of the respective generic view classes to perform
#CRUD operations on the Employee model:

class Employee(models.Model):
    name = models.CharField(max_lengeth=100)
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    class Meta:
        db_table = "employee"
    
# CreateView
# The CreateView class automates the creation of a new instance of the model.
# To provide a create view, use the sub class of CreateView:

from django.views.generic.edit import CreateView

class EmployeeCreate(CreateView):
    model = Employee
    fields = '__all__'
    success_url = "/employees/success/"
    
# A model form based on the model structure is created by this view and passed
#to the employeeCreate.html template:

<form method="post">
{% crsf_token %}
</table>
    {{form.as_table}}
</table>
    <input type="submit" value="Save">
</form>

#The URL path is updated by mapping the "create/" path to the as_view() method of this class

from .views import EmployeeCreate
urlpatterns = [
    ...
    path('create/', EmployeeCreate.as_view(), name = 'EmployeeCreate') ,
]

# When the client visits this URL, they are presented with the form. 
# The user fills and submits the employee details,, which are saved
#in the Employee table

#ListView

#Djangos django.views.generic.list module contains the definition of ListView
# class. Write its sub-class to render the list of model objects.

#The EmployeeList class is similar to the CreateView sub-class except its
#base class

from django.views.generic.list import ListView
class EmployeeList(ListView):
    model = Employee
    success_url = "/employees/success/"
    
# The template required for this view must be named employee_list.html
#Django sends the mdoel object in its context. Ussing the DTL loop
# syntax, you can display the list of employees

<ul>

        {% for object in object_list %}   
        <li>Name: {{ object.name }}</li>   
        <li>Email: {{ object.email }}</li>   
        <li>contact: {{ object.contact }}</li>  
        <br/> 
        {% endfor %} 
</ul>

# If the user visits http://localhost:/8000/employees/list
#, the browser lists all the rows in the employee table.

# DetailView
# The generic DeatailView is found in the django.views.generic.deatil module
# Now, create its sub-class, EmployeeDeail(much the same way as EmployeeList.
#note that this view shows the details of an object whose primary key is passed
#as an arguments in the URL. So, add the following path in the app's URL pattern

