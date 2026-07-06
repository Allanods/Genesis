from django.shortcuts import render,redirect,get_object_or_404
from myapp.models import *


# Create your views here.
def details(request):
    return render(request, 'blog-details.html')



def blog(request):
    return render(request, 'blog.html')

def home(request):
    if request.method == 'POST':
        mycontact = contact(
            name = request.POST['name'],
            email = request.POST['email'],
            subject = request.POST['subject'],
            message = request.POST['message']

        )
        mycontact.save()
        return render(request, 'index.html')
    
    else:
        return render(request, 'index.html')


def portfolio(request):
    return render(request, 'portfolio-details.html')

def services(request):
    return render(request, 'services-details.html')

def starter(request):
    return render(request, 'starter-page.html')

def show(request):
    all = contact.objects.all()
    return render(request, 'show.html', {'all': all})


def delete(request,id):
    mycontact = contact.objects.get(id = id)
    mycontact.delete()
    return redirect('/show')


def edit(request,id):
    editappointment = get_object_or_404(contact, id = id)

    if request.method == 'post':
        editappointment.name = request.Post.get('name')
        editappointment.email = request.Post.get('email')
        editappointment.subject = request.Post.get('subject')
        editappointment.message = request.Post.get('message')
        editappointment.save()
        return redirect('/show')
    else:
        return render(request, 'edit.html', {'editappointment':editappointment})







