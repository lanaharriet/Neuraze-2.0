from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def aurora_home(request):
    return render(request, "aurora/aurora.html")