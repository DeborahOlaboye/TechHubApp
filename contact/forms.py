from django import forms

class QuotationForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
        label='Your Name'
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
        label='Email Address'
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        label='Phone Number'
    )
    budget = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Budget Range'}),
        label='Budget Range'
    )
    service = forms.ChoiceField(
        choices=[
            ('', 'Select A Service'), 
            ('custom_software', 'Custom Software Development'),
            ('digital_marketing', 'Digital Marketing and SEO Services'),
            ('ecommerce', 'E-commerce Solutions'),
            ('it_support', 'IT and Support Services'),
            ('performance_optimization', 'Performance Optimization Services'),
            ('ui_ux', 'UI/UX Design and Branding Services')
        ],
        widget=forms.Select(attrs={'class': 'form-select'}),
        label='Select A Service'
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional Comments or Questions', 'style': 'height: 150px'}),
    )


class ContactForm(forms.Form):
    name = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
        label='Your Name'
    )
    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
        label='Email Address'
    )
    phone = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
        label='Phone Number'
    )
    message = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Additional Comments or Questions', 'style': 'height: 150px'}),
    )
