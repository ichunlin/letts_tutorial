from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from profiles import views

urlpatterns = [
    url(r'^profile/all$', views.profiles_list),
    url(r'^profile/$', views.add_profiles),
    url(r'^accounts/$', views.check_account),
]

urlpatterns = format_suffix_patterns(urlpatterns)