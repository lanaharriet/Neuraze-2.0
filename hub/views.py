from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from dashboard.models import UserActivity


@login_required
def hub(request):

    rooms = [
        {'name': 'Whisper Hall', 'url': 'whisper:whisper_home', 'locked': False},
        {'name': 'Mind Garden', 'url': 'mindgarden:mind_home', 'locked': False},
        {'name': 'Library Gate', 'url': 'library:library_home', 'locked': False},
<<<<<<< HEAD
        {'name': 'Community Space', 'url': 'community:feed', 'locked': False},
        {'name': 'Crystal Notes', 'url': 'crystal:crystal_home', 'locked': False},
=======
        {"name": "Community Space", "url": "community:feed", "locked": False},
        {"name":"Crystal Notes", "url":"crystal:crystal_home", "locked": False},
>>>>>>> 70e87ed73af5946502cd0243ee67d1880ad65587
        {'name': 'Aurora Voice', 'url': 'aurora:aurora_home', 'locked': False},
    ]

    total_points = UserActivity.objects.filter(
        user=request.user
    ).aggregate(Sum('points'))['points__sum'] or 0

    max_points = 100
    progress = min(int((total_points / max_points) * 100), 100)

    return render(request, 'hub/hub.html', {
        'rooms': rooms,
        'progress': progress
    })
