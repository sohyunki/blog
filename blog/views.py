from django.shortcuts import render,redirect,get_object_or_404
from .models import Write
from .forms import WriteForm

def index(request):
    all_write = Write.objects.all()
    return render(request, 'index.html',{'all_write':all_write})

def create(request):
    if request.method == "POST":
        create_form = WriteForm(request.POST)
        if create_form.is_valid():
            create_form.save()
            return redirect('index')
    else:
        create_form = WriteForm()
    return render(request,'create.html',{'create_form':create_form})

def detail(request, write_id):
    my_write = get_object_or_404(Write, id=write_id)
    return render(request,'detail.html',{'my_write':my_write})

def update(request, write_id):
    my_write = get_object_or_404(Write,id=write_id)
    if request.method == "POST":
        update_form = WriteForm(request.POST, instance= my_write)
        if update_form.is_valid():
            update_form.save()
            return redirect('index')
    else:
        update_form = WriteForm(instance=my_write)
    return render(request,'update.html',{'update_form':update_form})

def delete(request, write_id):
    my_write = get_object_or_404(Write,id = write_id)
    my_write.delete()
    return redirect('index')
