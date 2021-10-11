from django.shortcuts import render,redirect
 
# relative import of forms
from .models import MyModel
from .forms import MyForm
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.http import Http404
 
def create_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    form = MyForm(request.POST or None)
    if form.is_valid():
        form.save()
         
    context['form']= form
        
    return render(request, "create.html", context)



def list_view(request):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # add the dictionary during initialization
    context["dataset"] = MyModel.objects.all()
         
    return render(request, "list_view.html", context)



# pass id attribute from urls
def detail_view(request, id):
    # dictionary for initial data with
    # field names as keys
    
    try:
        context ={}
        context["data"]= MyModel.objects.get(id =id)
    except MyModel.DoesNotExist:
        raise Http404('Data does not exist')
 
    return render(request, "detail_view.html", context)
    

def update_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(MyModel, id = id)
 
    # pass the object as instance in form
    form =MyForm(request.POST or None, instance = obj)
 
    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
 
    # add form dictionary to context
    context["form"] = form
 
    return render(request, "update_view.html", context)

# delete view for details
def delete_view(request, id):
    # dictionary for initial data with
    # field names as keys
    context ={}
 
    # fetch the object related to passed id
    obj = get_object_or_404(MyModel, id = id)
 
 
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")
 
    return render(request, "delete_view.html", context)