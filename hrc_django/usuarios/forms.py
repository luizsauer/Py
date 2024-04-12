from django import forms

class LoginForms(forms.Form):

    username = forms.CharField(
        label = 'Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Ex.: seulogin',
            }
        )
    )

    senha = forms.CharField(
        label = 'Senha',
        required=True,
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        )
    )