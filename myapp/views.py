from django.shortcuts import render
from django.views import View

class Main(View):
    def get(self, request):
        
        return render(request, 'index.html')

def errorHandle(request):
    return render(request, '404.html')