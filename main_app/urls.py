from django.urls import path
from . import views

urlpatterns = [
    # setting url direction
    path('', views.HomeView.as_view(), name="Home"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('portfolio/', views.PortfolioView.as_view(),name="portfolio")
]
