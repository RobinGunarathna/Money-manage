from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'templates/index.index.html')

def add_expense(request):
    return render(request, 'templates/add_expense.html')