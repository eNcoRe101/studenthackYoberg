from django.shortcuts import render
from django.http import HttpResponse
from models import Yoscriber
from bloomberg import RandomCompany

# Create your views here.
def home(request):
  return HttpResponse("Hello World")

def yo(request):
  name = request.GET['username']
  result = "Yo! " + name
  try:
    user = Yoscriber.objects.get(yoname=name)
    number = user.phonenumber

    randomData = "" #actually get the random bloom data

    #sendText(number, randomData)
  except Yoscriber.DoesNotExist:
    result = result + ", oops..."

  shizz = RandomCompany.getRandomCompanyResponse()
  result = result + ", shizz - " + shizz

  return HttpResponse(result);


def receiveSMS(request):
  return HttpResponse("Dat SMS...")
