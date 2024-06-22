from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mango(request):
    return HttpResponse('<h1>MANGO</h1><h2 style="color:yellow">Mangoes are not only delicious but also offer a plethora of health benefits. Packed with vitamins, minerals, and antioxidants, mangoes support immune function, promote eye health, and aid digestion due to their high fiber content. They are also rich in vitamin C, which helps boost collagen production for healthy skin and supports the bodys natural defense against illnesses. Additionally, mangoes contain compounds like mangiferin, which have been studied for their potential anti-inflammatory and anti-cancer properties.</h2>')

def grapes(reuest):
    return HttpResponse('<h1>GRAPES</h1><h2 style="color:purple">Grapes, both delicious and nutritious, offer an array of health benefits. Rich in vitamins C and K, as well as antioxidants like resveratrol, grapes support immune function and promote healthy blood clotting. Their high water content aids hydration, while fiber contributes to digestive health.</h2>')