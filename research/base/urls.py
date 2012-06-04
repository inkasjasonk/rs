"""urlconf for the base application"""

from django.conf.urls.defaults import url, patterns


urlpatterns = patterns('research.base.views',
    url(r'^$', 'home', name='home'),
    url(r'^graphsafes', 'graph_safes', name='graph_safes'),
    url(r'^graphcomponent', 'graph_component', name='graph_component'),
    url(r'^raw/(?P<slug>.*)/$', 'raw', name='raw_data'),
)
