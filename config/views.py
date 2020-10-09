from django.shortcuts import render
def home(request):
    # context = {'title': 'homepage'}
    return render(request, "home.html", {})