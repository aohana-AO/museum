from django.urls import path

from dash import views

urlpatterns = [path("dash/", views.LineChartsView.as_view(), name="dash")]
