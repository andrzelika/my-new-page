from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    #url(r'', views.homepage ,name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('home.urls')),
]
