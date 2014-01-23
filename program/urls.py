
from django.conf.urls import patterns, url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from program import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^login/', views.LoginPage.as_view(), name="login"),
    url(r'^logout/', login_required( views.LogoutPage.as_view() ), name="logout"),
    url(r'^settings/', login_required( views.UserSettingsView.as_view() ), name="user settings"),

    url(r'problem/$', login_required( views.TeamProblemPage.as_view() ), name="problems"),
    url(r'problem/(\d+)$', login_required( views.ProblemDetailView.as_view() ), name="problem detail"),
    url(r'problem/(\d+)/submit/(\d+)$', login_required( views.ProblemExecutionView.as_view() ), name="problem execution")
)



