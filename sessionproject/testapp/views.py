from django.shortcuts import render

def name_view(request):
    return render (request , 'name.html')

def age_view(request):
    name = request.GET['uname']
    request.session['uname']=name
    response= render(request,'textapp/age.html' , {'name':name})
    return response

def qual_view(request):
    age = request.GET['uage']
    request.session['uage']=age
    response = render(request,'testapp/qualify.html')
    return response

def res_view(request):
    qual = request.GET['uqual']
    name = request.session.get('uname')
    age = request.session.get('uage')
    return render(request,'testapp/result.html',{'name':name,'age':age,'qual':qual})