from django.shortcuts import render

def name_view(request):
    return render (request , 'testapp/name.html')

def age_view(request):
    name = request.GET['uname']
    request.session['uname']=name
    return render(request,'testapp/age.html' , {'name':name})
    
def qual_view(request):
    age = request.GET['uage']
    request.session['uage']=age
    response = render(request,'testapp/qual.html')
    return response

def res_view(request):
    qual = request.GET['uqual']
    name = request.session.get('uname')
    age = request.session.get('uage')
    return render(request,'testapp/result.html',{'name':name,'age':age,'qual':qual})

# Create your views here.
