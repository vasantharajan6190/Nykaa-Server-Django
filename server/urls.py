"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from backend.views import simple_upload
from backend.views import newgame
from backend.views import signup
from backend.views import login
from backend.views import getgames
from backend.views import getgamebyid
from backend.views import loginplayer,signupplayer,allgamesforplayer,checkanswer,addpoints,getwinner
urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/',simple_upload),
    path('newgame/<int:user_id>/',newgame),
    path('signup/',signup),
    path('login/',login),
    path('game/<int:user_id>',getgames),
    path('gamebyid/<int:game_id>',getgamebyid),
    path('loginplayer/',loginplayer),
    path('signupplayer/',signupplayer),
    path('allgames/',allgamesforplayer),
    path('checkanswer/<int:gameid>',checkanswer),
    path('addpoints/',addpoints),
    path('getwinner/<int:gameid>',getwinner)
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
