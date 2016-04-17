from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'Newsletter.views.home', name='home'),
    
#    url(r'^contact/$', 'newsletter.views.contact', name='contact'),
#    url(r'^about/$', 'trydjango18.views.about', name='about'),
#    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', admin.site.urls),
    
]