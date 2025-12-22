#define URL route for index() view
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('bookings/', views.BookingViewSet.as_view({'get': 'list', 'post': 'create'})),
    path("api-token-auth/", obtain_auth_token),
]
