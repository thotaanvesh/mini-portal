"""
URL configuration for blogproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from testapp import views
import django
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.HomeView),
    path('detail/<int:id>/',views.DetailView),
    path('addblog/',views.addblog),
    path('accounts/',include('django.contrib.auth.urls')),
    path('signup/',views.signupview),
    path('myposts/',views.mypostview),
    path('myposts/<int:id>/',views.updateview),
    path('delete/<int:id>',views.deleteview),
]
if settings.DEBUG:  # Only add this in development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = views.notfoundview
