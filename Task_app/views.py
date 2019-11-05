from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.contrib import messages
from rest_framework.viewsets import ModelViewSet
from .serializers import Dataserializer #Fileviewserializer
#from os.path import isfile
import xlrd
from datetime import datetime, date
from .models import Data,File
# Create your views here.
import os

def savefile(request):
    filepath=request.FILES["doc"]
    File(doc=filepath).save()
    return redirect('/export/')
def export(request):
    print(os.getcwd())
    f=os.getcwd()
    qs = File.objects.all()
    filepath = ''
    for x in qs:
            filepath = str(x.doc.url)
    print(filepath)
    l=filepath.replace('/','\\')
    print(l)
    t=f+l
    print(t)
    book = xlrd.open_workbook(t, encoding_override='cp1252')
    sheet = book.sheet_by_index(1)
    nr_rows = sheet.nrows
    for row in range(1, nr_rows):
            row_value_list = [cell.value for cell in sheet.row(row)]
            a, b, c, d, e, f, g, h, i, j, k = tuple(row_value_list)
            a_dt = date.fromordinal(date(1900, 1, 1).toordinal() + int(a) - 2)
            b_dt = date.fromordinal(date(1900, 1, 1).toordinal() + int(b) - 2)
            Data(St_date=a_dt, End_date=b_dt, Task_Id=c, Task_desp=d, Wla_task_des=e, Resources=f, Quantity=g,Responsible_manager=h, Location=i, Chainage_from=j, Chainage_To=k).save()
    messages.success(request,"data saved")
    return redirect('/s/')

def getjson(request):
    qs = Data.objects.all()
    json_data = serialize('json', qs)
    return HttpResponse(json_data, content_type='application/json')
def show(request):
    qs = Data.objects.all()
    return render(request, 'uploadfile.html', {"data": qs})
class Dataviewset(ModelViewSet):
    queryset = Data.objects.all()
    serializer_class =Dataserializer
# class Fileviewset(ModelViewSet):
#     queryset = File.objects.all()
#     serializer_class = Fileviewserializer