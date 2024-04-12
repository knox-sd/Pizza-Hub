from django import forms
from .models import Pizza, Size #for Meta Class

# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label="Tooping 1", max_length=100 )
#     topping2 = forms.CharField(label="Tooping 2", max_length=100)
#     size = forms.ChoiceField(label='Size', choices=[('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large')])

class PizzaForm(forms.ModelForm):

    # size = forms.ModelChoiceField(queryset=Size.objects, empty_label=None, widget=forms.RadioSelect)
    # image = forms.ImageField() #upload image form
    # email = forms.EmailField()
    # url = forms.URLField()

    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']
        labels = {'topping1':'Topping 1', 'topping2':'Topping 2'}
        # widgets = {'topping1':forms.Textarea}
        # widgets = {'size':forms.CheckboxSelectMultiple}

class MultiplePizzaForm(forms.Form):
    number =forms.IntegerField(min_value=2, max_value=6)