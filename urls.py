from django.conf.urls import patterns, include, url

urlpatterns = patterns('hfhtml.views',
    url(r'^starbuzz$', 'index'),
#    url(r'(.+\.html)$', 'staticpage'),
)

urlpatterns += patterns('',
    url(r'(?P<template>.+\.html)$', 'django.views.generic.simple.direct_to_template'), 
)
