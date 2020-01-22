from django.shortcuts import render

# Create your views here. (java = controller)
def index(request):
    return render(request,'polls/index.html')