from __future__ import absolute_import

from django.conf.urls import patterns, url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from . import views

urlpatterns = patterns('',
    url(r'^$', login_required( views.ScoreboardView.as_view() ), name='scoreboard'),

    url(r'^settings\/?', login_required( views.UserSettingsView.as_view() ), name="user settings"),

    url(r'problem/$', login_required( views.ProblemListView.as_view() ), name="problem list"),
    url(r'problem/(\d+)$', login_required( views.ProblemDetailView.as_view() ), name="problem detail"),
    url(r'problem/(\d+)/submit/(\d+)$', login_required( views.ProblemExecutionView.as_view() ), name="problem execution"),
    url(r'problem/(\d+)/file$', login_required( views.TextFileGeneratorView.as_view() ), name="text file generator"),

)



