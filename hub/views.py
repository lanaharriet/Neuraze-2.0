from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def hub(request):

    rooms = [
        {'name': 'Whisper Hall', 'url': 'whisper:whisper_home', 'locked': False},
        {'name': 'Mind Garden', 'url': 'mindgarden:mind_home', 'locked': False},
        {'name': 'Library Gate', 'url': 'library:library_home', 'locked': False},
        {"name": "Community Space", "url": "community:feed", "locked": False},

        {'name': 'Aurora Voice', 'url': 'aurora:aurora_home', 'locked': False},
        # ⬇ ADD COMMUNITY ROOM HERE
    ]

    return render(request, 'hub/hub.html', {'rooms': rooms})
