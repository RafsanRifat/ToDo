from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from .forms import SignUpForm, CollectionUpdateForm, CollectionCreationForm, ItemCreationForm, ItemUpdateForm
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib import messages
from .models import Collection, Task


# Create your views here.

def test(request):
    return render(request, 'index.html')


def base(request):
    return render(request, 'auth_base.html')


def todo_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return redirect('home')
    else:
        return render(request, 'login.html')


def todo_logout(request):
    logout(request)
    return redirect('login')


def dashboard(request, *args, **kwargs):
    newcollection = CollectionCreationForm()
    if request.method == 'POST':
        newcollection = CollectionCreationForm(request.POST)
        if newcollection.is_valid():
            newcollection.instance.user = request.user
            newcollection.save()
    collections = Collection.objects.filter(user=request.user).all()  # show data only login users
    context = {'collections': collections, 'newcollection': newcollection}
    return render(request, 'dashboard.html', context)


def collections(request, id):
    collection = get_object_or_404(Collection, id=id, user=request.user)
    tasks = collection.task_set.all()
    form = CollectionUpdateForm(
        instance=collection)  # instance hoilo ei form er property, orthat ei form er moddhe kon kon value show korbe
    if request.method == 'POST':
        form = CollectionUpdateForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()

    # create new item
    newitem = ItemCreationForm()
    if request.method == "POST":
        newitem = ItemCreationForm(request.POST)
        if newitem.is_valid():
            newitem.instance.collection = collection
            newitem.save()

    #update item
    # task = get_object_or_404(Task, id=id)
    # for task in tasks:
    #     task.form = ItemCreationForm(instance=task)
    #     task_id = task.id
    #     print(task_id)
    itemUpdate = ItemUpdateForm() #instance=task
    # if request.method == 'POST':
    #     task_id = request.POST.get('task-id')
    #     print(task_id)
        # itemUpdate = ItemUpdateForm(request.POST, task_id)
        # itemUpdate = ItemUpdateForm(request.POST, instance=get_object_or_404(Task, id=task_id))
        # if itemUpdate.is_valid():
        #     itemUpdate.save()

    context = {'tasks': tasks, 'collection': collection, 'form': form, 'newitem': newitem, 'itemUpdate': itemUpdate}
    return render(request, 'collection_list.html', context)


def udpate_task(request, id):
    if request.method == 'POST':
        itemUpdateForm = ItemUpdateForm(request.POST, instance=get_object_or_404(Task, id=id))
        if itemUpdateForm.is_valid():
            itemUpdateForm.save()
            return redirect('dashboard')
    return render(request, 'collection_list.html')

def deleteCollection(request, id):
    collection = get_object_or_404(Collection, id=id, user=request.user)
    if request.method == "POST":
        collection.delete()
        return redirect('dashboard')


def deleteTask(request, id):
    task = get_object_or_404(Task, id=id)
    collection = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return redirect('dashboard')


# def updateTask(request, id):
#     # task = Task.objects.get(id=id)
#     task = get_object_or_404(Task, id=id)
#     itemUpdate = ItemUpdateForm(instance=task)
#     # if request.method == 'POST':
#     #     itemUpdate = ItemUpdateForm(request.POST, instance=task)
#     #     if itemUpdate.is_valid():
#     #         itemUpdate.save()
#     context = {'task': task, 'itemUpdate': itemUpdate}
#     return render(request, 'collection_list.html', context)


@csrf_protect
def todo_signup(request):
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if User.objects.filter(username=request.POST['username']).exists():
            messages.warning(request, 'This username is already used')
        else:
            if signup_form.is_valid():
                signup_form.save()
                return redirect('login')
    else:
        signup_form = SignUpForm()
    return render(request, 'signup.html', {'signup_form': signup_form})
