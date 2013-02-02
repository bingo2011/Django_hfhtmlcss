from django.conf.urls import patterns, include, url

urlpatterns = patterns('hfhtml.views',
    url(r'^starbuzz$', 'index'),
)
