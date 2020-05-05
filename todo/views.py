from django.shortcuts import render, redirect
from .models import todo_item

def home(request):
    if todo_item.objects.all() == None:
        return render(request, 'home.html', context={"value":"No todo item found"})
    else:
        val = todo_item.objects.all()
        context = {
            "val":val,
        }
        return render(request, 'home.html', context={"val":val})

def push(request):

    if request.method == 'POST':
        val = request.POST['context']
    todo = todo_item.objects.create(content = val)
    todo.save()
    return redirect('/')

def delete(request, id):
    delete_val = todo_item.objects.get(id = id)
    delete_val.delete()
    return redirect("/")


   
