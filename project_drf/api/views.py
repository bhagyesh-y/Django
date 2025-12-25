from django.shortcuts import render
from django.http import JsonResponse


def studentsview(request):
    students={
        'id':1,
        'name':'bhagyesh',
        'class':'CS'
    }
    return JsonResponse(students)
    
