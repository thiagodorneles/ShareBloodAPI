from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/account', include('account.urls', namespace='account')),
    url(r'^api/v1/location', include('location.urls', namespace='location')),
    url(r'^api/v1/donation', include('donation.urls', namespace='donation')),
)
