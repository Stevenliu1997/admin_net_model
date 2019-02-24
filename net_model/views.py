#coding:utf-8
import os
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from net_model.models import CSV
from net_model.models import PatientInfo
from net_model.models import DoctorUser
from net_model.models import PatientRecord
from net_model.models import CT
from net_model.models import Node

import json
import datetime
from django.core import serializers

import pydicom

def Read_Dicom_Info():
    filename = ''
    ctinfo = pydicom.read_file(filename)
    (filepath, tempfilename) = os.path.split(filename)
    shotname, extension = os.path.splitext(tempfilename)
    CTID = shotname
    ct = {
        'CTID': CTID,
        'CTDate': ctinfo.date,
        'Patient': ctinfo.PatientID
    }
    #todo read dicom as a try
    #CT.objects.create(**ct)
    return

def index(request):
    return render(request, 'home.html')

def Get_Search_result(request):
    if request.method == 'GET':
        userid = request.GET.get('userId')
        obj = PatientInfo.objects.get(PatientID=userid)
        return HttpResponse(json.dumps(
            {'userName': obj.PatientName}
        ))

def Get_Patient_Info(request):
    if request.method == 'GET':
        a = request.GET.get('message')
        Patient_List = PatientInfo.objects.get(PatientID=a)
        ct = CT.objects.get(PatientID=a)
        #todo the queryset api get or filter
        return HttpResponse(
            json.dumps({
                'id': Patient_List.PatientID,
                'name': Patient_List.PatientName,
                'PatientSex': Patient_List.PatientSex,
                'time': ct.CTDate
            })
        )

def Get_Nodule_Info(request):
    #todo can not past the 3D pic
    if request.method == 'GET':
        ctid = request.GET.get('CTId')
        record = PatientRecord.objects.get(CTID=ctid)
        position = record.PartInfo
        node_list = Node.objects.filter(CTID=ctid)
        #todo 分割再封装QuerySet

        return HttpResponse(
            json.dumps(
                {
                    'part':position,
                    'nodeinfo':{
                        'position': (node_list.Node_x,node_list.Node_y,node_list.Node_z),
                        'judge': node_list.illjudge,
                        'NodeID': node_list.NodeID
                    }
                }
            )

        )

def Edit_Patient_Ill(request):
    if request.method == 'GET':
        CTID = request.GET.get('CTId')
        entityInfo = PatientRecord.objects.get(CTID=CTID)
        return HttpResponse(
            json.dumps(
                {
                    'PatientID': entityInfo.PatientID,
                    'PartInfo': entityInfo.PartInfo,
                    'Description': entityInfo.Description
                }
            )
        )

def Add_Ill_Info(request):
    if request.method == 'POST':
        entityInfo = request.POST.get()
        nowTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        RecordID = nowTime.format(entityInfo.PatientID)
        record = {
            'RecordId': RecordID,
            'PatientID': entityInfo.patientid,
            'Description': entityInfo.description,
            'MedicalTime': entityInfo.time,
            'PartInfo': entityInfo.position,
            'CTID': ' '
        }
        PatientRecord.objects.create(**record)
        return HttpResponse(
            json.dumps({'msg': 'sucess to store'})
        )

list = {}
json.dumps({

})