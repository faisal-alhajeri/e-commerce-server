from django import forms 
from product.models import Product



class ProductCreateForm(forms.ModelForm):
    # categories = 
    class Meta:
        model = Product
        fields = ['name', 'description', 'price']