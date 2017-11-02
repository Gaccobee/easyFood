from django.conf.urls import url, include
from django.contrib import admin

from home import urls as home_urls
from account import urls as account_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(home_urls)),
    url(r'^account/', include(account_urls))
]
