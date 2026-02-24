from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.shortcuts import redirect

def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    return HttpResponse(template.render({'mymembers': mymembers}, request))

def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template('details.html')
    return HttpResponse(template.render({'mymember': mymember}, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def add(request):
    return HttpResponse(loader.get_template('add.html').render())

def addrecord(request):
    member = Member(
        firstname=request.POST['first'],
        lastname=request.POST['last'],
        phone=request.POST['phone'],
        joined_date=request.POST['joined_date']
    )
    member.save()
    return redirect('members')

def delete(request, id):
    Member.objects.get(id=id).delete()
    return redirect('members')

def update(request, id):
    mymember = Member.objects.get(id=id)
    return HttpResponse(loader.get_template('update.html')
                        .render({'mymember': mymember}, request))

def updaterecord(request, id):
    member = Member.objects.get(id=id)
    member.firstname = request.POST['first']
    member.lastname = request.POST['last']
    member.phone = request.POST['phone']
    member.joined_date = request.POST['joined_date']
    member.save()
    return redirect('members')

# Create your views here.
