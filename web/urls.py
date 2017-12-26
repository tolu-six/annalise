from django.conf.urls import url

from .views import (
    SignInView, DashboardView, ProfileView,
    IndexView, RegisterView, RequestView
)


urlpatterns = [
    url(r'^signin/', SignInView.as_view(), name='signin'),
    url(r'^dashboard/', DashboardView.as_view(), name='dashboard'),
    url(r'^profile/', ProfileView.as_view(), name='profile'),
    url(r'^request/', RequestView.as_view(), name='request'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^$', IndexView.as_view(), name='index'),
]
