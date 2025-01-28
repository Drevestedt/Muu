from django.shortcuts import render

# Create your views here.
def base(response):
  return render(response, "base.html", {})

def home(response):
  return render(response, "home.html", {})
