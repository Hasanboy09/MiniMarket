from django.urls import path

from apps.views import RegisterFormVIew, ProductListView, LoginFormVIew, ProductDetailView, ProductDeleteView, \
    ProductUpdateView, ProfileTemplateView

urlpatterns = [
    path('', RegisterFormVIew.as_view(), name='register'),
    path('login', LoginFormVIew.as_view(), name='login'),

]

urlpatterns += [
    path('products', ProductListView.as_view(), name='home'),
    path('product-detail/<int:pk>', ProductDetailView.as_view(), name='product-detail'),
    path('product-update/', ProductUpdateView.as_view(), name='product-update'),
    path('product-delete/<int:pk>', ProductDeleteView.as_view(), name='product-delete'),
]

urlpatterns += [
    path('profile' , ProfileTemplateView.as_view(), name='profile')
]