from django.shortcuts import render
from django.shortcuts import redirect, render
import webbrowser

def home(request):
    return render(request, 'grafico/index.html')

# Create your views here.
