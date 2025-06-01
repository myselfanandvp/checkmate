from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model=Product
        fields = '__all__'
        
    def save(self, commit =True):
        product= super().save(commit)        
        if commit:
            product.save()