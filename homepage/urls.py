from django.conf.urls import patterns, include, url
from homepage.views import ItemList, ItemDetailView, ajax
from haystack.views import SearchView
from haystack.forms import SearchForm

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', ItemList.as_view()),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^item/(?P<pk>\w+)/', ItemDetailView.as_view()),
    url(r'^search/$', ajax),

)
"""
urlpatterns += patterns('',
    (r'^search/', SearchView(form_class = SearchForm)),
)"""