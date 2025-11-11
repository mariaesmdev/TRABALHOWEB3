from django import forms

class ContactForm(forms.Form):
    nome = forms.CharField(max_length=100, label="Nome", widget=forms.TextInput(attrs={
        "id": "nome",
        "placeholder": "Seu nome",
        "required": True,
        "class": "form-control"
    }))
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={
        "id": "email",
        "placeholder": "seu@exemplo.com",
        "required": True,
        "class": "form-control"
    }))
    mensagem = forms.CharField(label="Mensagem", widget=forms.Textarea(attrs={
        "id": "mensagem",
        "rows": 6,
        "placeholder": "Escreva sua mensagem...",
        "required": True,
        "class": "form-control"
    }))