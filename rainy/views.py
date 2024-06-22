from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def pear(request):
    return HttpResponse('<h1>PEAR</h1><h2 style="color:lightgreen">Pears are not only delicious but also offer numerous health benefits. Rich in fiber, they aid digestion and promote gut health, helping to prevent constipation and maintain a healthy weight. Pears also contain antioxidants, such as vitamin C and copper, which help boost the immune system and fight inflammation.</h2>')

def blueberry(request):
    return HttpResponse('<h1>BLUEBERRY</h1><h2 style="color:darkblue">Blueberries are small but mighty fruits packed with nutrients and health benefits. They are rich in antioxidants, particularly flavonoids, which help protect the body from oxidative stress and inflammation, reducing the risk of chronic diseases like heart disease, cancer, and diabetes. Blueberries are also high in fiber, aiding digestion and promoting gut health.</h2>')