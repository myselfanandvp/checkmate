from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm
from .models import Product

# Create your views here.
@method_decorator(never_cache, name='dispatch')
class CreateProduct(LoginRequiredMixin,View):
    login_url='loginurl'
    template_name = 'createproduct.html'
    is_productpage = True
    def get(self, request):
        form=ProductForm()        
        return render(request, self.template_name, {'form': form, 'is_productpage': self.is_productpage})
      

    def post(self, request):
        newproduct = ProductForm(request.POST, request.FILES)
        if newproduct.is_valid():
            newproduct.save()
            return redirect('listproducturl')
        return render(request, self.template_name, {'form': newproduct, 'is_productpage': self.is_productpage})

@method_decorator(never_cache, name='dispatch')
class ListProduct(LoginRequiredMixin,View):
    login_url='loginurl'
    is_productpage = True
    template_name = 'productlist.html'

    def get(self, request): 
        recent_edited = request.session.get("recent_edited_products",[])       
        products = Product.objects.all()
        return render(request,self.template_name , {'products': products, 'is_productpage': self.is_productpage})

        


@method_decorator(never_cache, name='dispatch')
class EditProduct(LoginRequiredMixin,View):
    login_url='loginurl'
    is_productpage = True
    template_name = 'producteditpage.html'
    
    def get(self, request, product_id):        
        product = get_object_or_404(Product, id=product_id)
        editedproduct = ProductForm(instance=product)
        return render(request,self.template_name,{'form':editedproduct})
        
    
    def post(self,request,product_id):       
        product = get_object_or_404(Product,id=product_id)
        form = ProductForm(request.POST,request.FILES,instance=product)
        if form.is_valid():
            form.save()
            return redirect("listproducturl")
        return render(request,self.template_name,{'form':form})
    
    
class DeleteProduct(LoginRequiredMixin,View):
    login_url='loginurl'
    template_name='productlist.html'
    is_productpage=True
    def post(self,request,product_id):
        product=get_object_or_404(Product,id=product_id)
        if product:
            product.delete()
            return redirect('listproducturl')
        return render(request,self.template_name,{'is_productpage':self.is_productpage})
    
    def get(self,request,product_id=None):
        return redirect("listproducturl")
        
            
            
            

        
