from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def StudentFunctionBasedAPI(request):
    if request.method == 'GET':
        entered_data = request.data    #enter_data will be in python format(dictionary)
        entered_data_id = entered_data.get('id', None)
        
        if entered_data_id is not None:
            stu_obj = Students.objects.filter(id = entered_data_id)
            stu_seri = StudentSerializer(stu_obj, many = True)
            return Response(stu_seri.data)
        
        stu_objs = Students.objects.all()
        stu_seri = StudentSerializer(stu_objs, many=True)
        # print("stu_objs",stu_objs)
        # print("***********")
        # print("stu_seri",stu_seri)
        return Response(stu_seri.data)
    
    elif request.method == 'POST':
        entered_data = request.data
        stu_seri = StudentSerializer(data = entered_data)
        # print("entered_data",entered_data)
        # print("***********")
        # print("stu_seri",stu_seri)
        if stu_seri.is_valid():
            stu_seri.save()
            return Response(stu_seri.data)
        else:
            return Response(stu_seri.errors)
        
