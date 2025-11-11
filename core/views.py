import logging

from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage

from .forms import ContactForm

logger = logging.getLogger(__name__)

def index(request):
    return render(request, "index.html")

def sobre(request):
    return render(request, "sobre.html")

def projetos(request):
    return render(request, "projetos.html")

def doacao(request):
    return render(request, "doacao.html")

def contato(request):
    """
    Handle contact form: GET -> show form, POST -> validate & send email, then redirect with message.
    Uses EmailMessage to set Reply-To in a way compatível com várias versões do Django.
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            remetente = form.cleaned_data["email"]
            mensagem = form.cleaned_data["mensagem"]

            subject = f"Contato pelo site — {nome}"
            body = f"Nome: {nome}\nE-mail: {remetente}\n\nMensagem:\n{mensagem}"

            from_email = getattr(settings, "DEFAULT_FROM_EMAIL", "no-reply@example.com")
            to_email = getattr(settings, "DEFAULT_TO_EMAIL", from_email)

            try:
                # Usa EmailMessage com header Reply-To para compatibilidade
                email_msg = EmailMessage(
                    subject=subject,
                    body=body,
                    from_email=from_email,
                    to=[to_email],
                    headers={"Reply-To": remetente},
                )
                email_msg.send(fail_silently=False)

                messages.success(request, "Mensagem enviada com sucesso — obrigado(a)!")
                return redirect("contato")
            except Exception as e:
                logger.exception("Erro ao enviar email do formulário de contato")
                if getattr(settings, "DEBUG", False):
                    messages.error(request, f"Ocorreu um erro ao enviar a mensagem: {e}")
                else:
                    messages.error(request, "Ocorreu um erro ao enviar a mensagem. Tente novamente mais tarde.")
        else:
            messages.error(request, "Por favor corrija os erros no formulário antes de enviar.")
    else:
        form = ContactForm()

    return render(request, "contato.html", {"form": form})