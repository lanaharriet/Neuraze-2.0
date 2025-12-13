from django.contrib import admin
from django.urls import path, include
from NeurAze import views  # needed for ai_chatbot_api

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts (signup/login/logout)
    # Combines both Django auth and your custom accounts app
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Main hub
    path('', include(('hub.urls', 'hub'), namespace='hub')),

    # Feature Rooms
    path('whisper/', include(('whisper.urls', 'whisper'), namespace='whisper')),
    path('mindgarden/', include(('mindgarden.urls', 'mindgarden'), namespace='mindgarden')),
    path('library/', include(('library.urls', 'library'), namespace='library')),
    path('crystal/', include(('crystal.urls', 'crystal'), namespace='crystal')),
    path('community/', include(('community.urls', 'community'), namespace='community')),

    # Dashboard
    path('dashboard/', include('dashboard.urls')),

    # AI chatbot API
    path('chatbot-reply/', views.chatbot_reply, name='chatbot_reply'),
]
