from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from category import views

urlpatterns = [
    url(r'^category/$', views.category_list),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)