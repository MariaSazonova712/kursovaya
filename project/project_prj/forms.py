from .models import Product
from django.forms import ModelForm, TextInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["number","name", "price", "quantity", "manufacturer"]
        widgets = {
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите номер'
            }),
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите наименование'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите цену'
            }),

            "quantity": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите массу'
            }),
            "manufacturer": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите производителя'
            }),
        }
