
from django.urls import path

from apps.views import RegisterFormVIew, ProductListView, LoginFormVIew

urlpatterns = [
    path('', RegisterFormVIew.as_view(), name='register'),
    path('login', LoginFormVIew.as_view(), name='login'),

]

urlpatterns += [
    path('products', ProductListView.as_view(), name='home'),
]
