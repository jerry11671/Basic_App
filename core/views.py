from django.shortcuts import render
from django.http import HttpResponse

def home(index):
    return HttpResponse('<b>My name is Jerry</b>')
