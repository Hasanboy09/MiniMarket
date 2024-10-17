from django.contrib.auth import login
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, ListView, DetailView

from apps.forms import RegistrationForm, LoginForm
from apps.models import Product, Category


# Create your views here.
class RegisterFormVIew(FormView):
    form_class = RegistrationForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('login')  # after register

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class LoginFormVIew(FormView):
    form_class = LoginForm
    template_name = 'auth/login.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.find_user
        login(self.request, user)
        return super().form_valid(form)


class ProductListView(ListView):
    queryset = Product.objects.all()
    context_object_name = 'products'
    template_name = 'product/product-list.html'

    def get_context_data(self, *args, **kwargs):
        data = super().get_context_data(*args, **kwargs)
        category_id = self.request.GET.get('category_id')
        data['categories'] = Category.objects.all()
        if category_id:
            data['products'] = data.get('products').filter(category_id=category_id)
        return data


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/product-detail.html'
    context_object_name = 'product'


class ProductDeleteView(View):
    def get(self, request, pk):
        Product.objects.filter(pk=pk).first().delete()
        return redirect('home')


class ProductUpdateView(View):
    def post(self, request):
        product_id = request.GET.get('product_id')
        quantity = request.POST.get('quantity')
        try:
            product = Product.objects.get(id=product_id)
            product.quantity = int(quantity)
            product.save()
        except Product.DoesNotExist:
            pass
        return redirect('home')

