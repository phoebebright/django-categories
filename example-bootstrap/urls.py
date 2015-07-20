from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from simpletext.views import *

import os

ROOT_PATH = os.path.dirname(os.path.dirname(__file__))

urlpatterns = patterns('',

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^categories/', include('categories.urls')),
    (r'^cats/', include('categories.urls')),

    (r'^static/categories/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': ROOT_PATH + '/categories/media/categories/'}),

    # (r'^static/editor/(?P<path>.*)$', 'django.views.static.serve',
    #     {'document_root': ROOT_PATH + '/editor/media/editor/',
    #      'show_indexes':True}),

     (r'^static/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': os.path.join(ROOT_PATH, 'example', 'static')}),
                       )


urlpatterns += patterns('simpletext.views',
    url(r'list/$', TxtListView.as_view(), name='txt-list'),
    url(r'add/$', TxtAddView.as_view(), name='txt-add'),
    url(r'(?P<pk>\d+)/$', TxtDetailView.as_view(), name='txt-view'),
    url(r'edit/(?P<pk>\d+)/$', TxtEditView.as_view(), name='txt-edit'),



)
