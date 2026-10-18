from django.shortcuts import render

def dashboard_admin(request):
    return render(request, "panel.html")
