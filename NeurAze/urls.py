from django.contrib import admin
from django.urls import path, include
from . import views  
#from django.http import HttpResponse

urlpatterns = [

    #path('', lambda request: HttpResponse("NEURAZE WORKING ✅")),
    
    path('admin/', admin.site.urls),

    # ✅ ADD THIS (CRITICAL)
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),

    # Main hub
    path('', include(('hub.urls', 'hub'), namespace='hub')),

    # Feature modules
    path('whisper/', include(('whisper.urls', 'whisper'), namespace='whisper')),
    path('mindgarden/', include(('mindgarden.urls', 'mindgarden'), namespace='mindgarden')),
    path('library/', include(('library.urls', 'library'), namespace='library')),
    path('crystal/', include(('crystal.urls', 'crystal'), namespace='crystal')),
    path('community/', include(('community.urls', 'community'), namespace='community')),
    path('aurora/', include(('aurora.urls', 'aurora'), namespace='aurora')),

    path('dashboard/', include('dashboard.urls')),

    # chatbot (if needed)
    path('chatbot-reply/', views.chatbot_reply, name='chatbot_reply'),
]