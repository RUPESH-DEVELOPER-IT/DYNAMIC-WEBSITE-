from django.shortcuts import render,redirect

from ap.models import tn

# Create your views here.

def home(request):
    if request.method == 'POST':
        q=request.POST['a']
        w=request.POST['s']
        e=tn()
        e.name=q
        e.numbers=w
        e.save()
        return redirect('view')

    return render(request, 'home.html')

def view(request):
    v=tn.objects.all()
    return render(request,'view.html',{'v':v})

def update(request,id):
    f=tn.objects.get(id=id)
    if request.method == 'POST':
        i=request.POST['p']
        u=request.POST['o']
        f.name=i
        f.numbers=u
        f.save()
        return redirect('view')
    return render(request,'update.html',{'c':f})

def delete(request,id):
    j=tn.objects.get(id=id)
    j.delete()
    return redirect('view')

