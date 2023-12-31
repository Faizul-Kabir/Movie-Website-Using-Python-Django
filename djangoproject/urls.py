
from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from descriptions import views as descriptions_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('descriptions/', include('descriptions.urls')),
    path('account/', include('account.urls')),
    path('about/', views.about),
    path('',descriptions_views.descriptions_list,name="home"),

]

urlpatterns+=staticfiles_urlpatterns()
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)