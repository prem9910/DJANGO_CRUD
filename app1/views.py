from multiprocessing import context
from django.shortcuts import redirect, render
from .forms import UserForm
from .models import User


def Home(request):
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        form.save()
        form=UserForm()
    
    data=User.objects.all()

    


    context={
        'form':form,
        'data':data,
    }
    return render(request,'app1/index.html',context)

def Delete_record(request,id):
    a=User.objects.get(pk=id)
    a.delete()
    return redirect('/')
    

# Update View
def Update_Record(request,id):
    if request.method=='POST':
        data=User.objects.get(pk=id)
        form=UserForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
    else:

        data=User.objects.get(pk=id)
        form=UserForm(instance=data)
    context={
        'form':form,
    }
    return render (request,'app1/update.html',context)