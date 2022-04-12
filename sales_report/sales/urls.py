from django.urls import path
from . import views
from .views import SalesListView, SalesDetailView

app_name = 'sales'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('sales_list/', SalesListView.as_view(), name='list'),
    path('sales/<pk>/', SalesDetailView.as_view(), name='detail')
]