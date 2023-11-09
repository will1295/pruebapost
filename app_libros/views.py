from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from .formularios.form1 import NameForm


def inicio(request):
    return render(request,"home.html")

def get_nombre(request):
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect()
    else:
        form = NameForm()
    return render(request,"formulario.html",{"form":form})
