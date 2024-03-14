from django import forms
from .models import ApplyForm
from datetime import date, timedelta
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget

class ApplyFormForm(forms.ModelForm):
    class Meta:
        model = ApplyForm
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'w-full bg-gray-100 text-gray-900 mt-2 p-2 rounded-lg focus:outline-none focus:shadow-outline',
                'required': True,
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'w-full bg-gray-100 text-gray-900 mt-2 p-2 rounded-lg focus:outline-none focus:shadow-outline',
                'required': True,
            }),
            'country': forms.Select(attrs={
                'class': 'w-full bg-gray-100 text-gray-900 mt-2 p-2 rounded-lg focus:outline-none focus:shadow-outline',
                'required': True,  # Make it required
            }),
            'interested_for': forms.Select(attrs={
                'class': 'w-full bg-gray-100 text-gray-900 mt-2 p-2 rounded-lg focus:outline-none focus:shadow-outline',
                'required': True,
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full bg-gray-100 text-gray-900 mt-2 p-2 rounded-lg focus:outline-none focus:shadow-outline',
                'required': True,
            }),
            'phonenumber': forms.TextInput(attrs={
                'class': 'w-full bg-gray-100 text-gray-900 mt-2 p-2 rounded-lg focus:outline-none focus:shadow-outline',
                'required': True,
                'pattern': '',  # Placeholder for the pattern attribute
            }),

            'date_of_birth': forms.DateInput(attrs={
                'class': 'w-full bg-gray-100 text-gray-900 mt-2 p-2 rounded-lg focus:outline-none focus:shadow-outline',
                'type': 'date',
                'max': (date.today() - timedelta(days=18*365)).strftime('%Y-%m-%d'),
                'required': True,
            }),
            'want_to_work': forms.Select(attrs={
                'class': 'w-full bg-gray-100 text-gray-900 mt-2 p-2 rounded-lg focus:outline-none focus:shadow-outline',
                'required': True,
            }),
            'highest_education': forms.Select(attrs={
                'class': 'w-full bg-gray-100 text-gray-900 mt-2 p-2 rounded-lg focus:outline-none focus:shadow-outline',
                'required': True,
            }),
            'earliest_start_date': forms.DateInput(attrs={
                'class': 'w-full bg-gray-100 text-gray-900 mt-2 p-2 rounded-lg focus:outline-none focus:shadow-outline',
                'type': 'date',
                'min': (date.today()).strftime('%Y-%m-%d'),
                'required': True,
            }),
            'national_id': forms.TextInput(attrs={
                'class': 'w-full bg-gray-100 text-gray-900 mt-2 p-2 rounded-lg focus:outline-none focus:shadow-outline',
                'required': True,
            }),
            'position': forms.TextInput(attrs={
                'class': 'w-full bg-gray-100 text-gray-900 mt-2 p-2 rounded-lg focus:outline-none focus:shadow-outline',
                'required': True,
            }),

            'cv': forms.FileInput(attrs={
                'class': 'w-full bg-gray-100 text-gray-900 mt-2 p-2 rounded-lg focus:outline-none focus:shadow-outline',
                'accept': '.pdf,.doc,.docx',
                'required': True,
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'w-full bg-gray-100 text-gray-900 mt-2 p-2 rounded-lg focus:outline-none focus:shadow-outline',
                'accept': 'image/*',
                'required': True,  # This can be True or False based on your requirements
            }),
        }
