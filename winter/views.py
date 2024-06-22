from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def apple(request):
    return HttpResponse('<h1>APPLE</h1><h2 style="color:red">Apples are a good source of nutrients, including fiber, vitamin C, and antioxidants which can help support healthy digestion, brain health, and weight management. There is evidence that apples can also protect against certain chronic diseases, including cancer, heart disease, and type 2 diabetes.</h2>')

def guava(request):
    return HttpResponse('<h1>GUAVA</h1><h2 style="color:green">Guava fruit offers a plethora of health benefits packed into its deliciously tropical taste. Rich in vitamin C, it boosts immunity and promotes skin health, aiding collagen production. Its high fiber content aids digestion, preventing constipation and promoting gut health. Guava is also a good source of antioxidants, helping to neutralize free radicals and reduce the risk of chronic diseases.</h2>')