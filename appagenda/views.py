from django.shortcuts import render

# Create your views here.
def home(request):
    ususario = "Francisco"
    context = {
        'usuario': ususario,
        'dtnascimento': '1975-10-04'
    }
    return render(request,'appagenda/home.html', context)
