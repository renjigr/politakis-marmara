"""politakis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from work import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.IndexView.as_view(),name='home'),
    path('work/',views.WorkListView.as_view(),name='work'),
    path('work/bath',views.BathListView.as_view(),name='bath'),
    path('work/cousines',views.CousinesListView.as_view(),name='cousines'),
    path('work/fireplaces',views.FireplaceListView.as_view(),name='fireplaces'),
    path('work/floor',views.FloorListView.as_view(),name='floor'),
    path('work/out',views.OutListView.as_view(),name='out'),
    path('work/stairs',views.StairsListView.as_view(),name='stairs'),
    path('work/art',views.ArtListView.as_view(),name='art'),
    path('work/marble',views.MarbleListView.as_view(),name='marble'),
    path('work/granite',views.GraniteListView.as_view(),name='granite'),
    path('work/quartz',views.QuartzListView.as_view(),name='quartz'),
    path('work/<slug>/',views.SingleView.as_view(), name ='work_details'),
    path('where/',views.WhereView.as_view(), name ='where'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
