# Instruções rápidas para agentes de código (Copilot / IA)

Projeto: site Django simples (ONG) — `core` app + `config` settings. Use este guia para contexto rápido e regras práticas ao editar/implementar.

Resumo rápido
- Estrutura: monolito Django (versão 5.x). Entrypoint: `manage.py`. App principal: `core/` (views, forms, templates, static).
- Banco local: `db.sqlite3` (configurado em `config/settings.py`). Emails em dev vão para console (`EMAIL_BACKEND`).

Contrato mínimo
- Inputs: alterações em `core/` (views, templates, static, forms) ou `config/settings.py`.
- Outputs esperados: páginas renderizadas em `core/templates/`, assets servidos de `core/static/`, e mensagens de sucesso/erro via Django messages.
- Erros: logue via `logger = logging.getLogger(__name__)` (padrão já usado em `core/views.py`).

Onde olhar primeiro (exemplos)
- Rotas/URLs: `core/urls.py` — adiciona novas páginas aqui.
- Views: `core/views.py` — views são funções simples; veja `contato` para padrão POST/GET e envio de email.
- Forms: `core/forms.py` — `ContactForm` é usado pelo view `contato`.
- Templates: `core/templates/` — templates são referenciados diretamente (TEMPLATES.DIRS aponta para essa pasta).
- Static: `core/static/` — CSS/JS/imagens referenciadas durante DEBUG via `STATICFILES_DIRS`.
- Config: `config/settings.py` — ajustes de DEBUG, EMAIL, ALLOWED_HOSTS; note duplicação de blocos TEMPLATES/STATICFILES (evitar alterações conflitantes).

Fluxos de desenvolvedor essenciais
- Levantar ambiente local:
  - python manage.py migrate
  - python manage.py runserver
- Criar superuser: `python manage.py createsuperuser` (se precisar de admin).
- Console de email: mensagens do formulário `contato` aparecem no terminal porque `EMAIL_BACKEND` está configurado para `console`.

Padrões e convenções do projeto
- Templates não estão em subpastas por app — coloque o template diretamente em `core/templates/` e renderize como `render(request, "nome.html")`.
- Ao adicionar uma página:
  1. Criar template em `core/templates/` (ex: `nova.html`).
  2. Criar view em `core/views.py` (função que retorna `render(request, "nova.html")`).
  3. Registrar rota em `core/urls.py`.
  4. Colocar assets em `core/static/{css,js,assets}` e referenciar com `{% static %}`.
- Formulários: preferir `forms.Form` para formulários simples (veja `ContactForm`).
- Emails: `contato` usa `EmailMessage` e seta header `Reply-To` — preserve esse padrão ao portar/alterar envio.

Integrações e pontos sensíveis
- Banco: `db.sqlite3` está no repo para desenvolvimento; ao modificar models, rode `makemigrations` + `migrate` e inclua migrations no PR.
- Emails: variável `DEFAULT_TO_EMAIL` em `config/settings.py` controla o destino — útil para testes locais (hoje aponta para um e-mail real). Em dev o backend é `console`.
- Segurança: `DEBUG = True` no settings atualmente. Para deploy, ajustar `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS` e backend de email.

Pull requests e mudanças de infra
- Incluir migrations quando modelos mudarem.
- Testes: rodar `python manage.py test` (não há suíte extensa hoje, mas adicione testes ao alterar lógica importante).

Notas finais rápidas
- Evite reestruturar `TEMPLATES`/`STATICFILES_DIRS` sem checar código de templates e `settings.py` — há blocos duplicados que podem confundir.
- Se precisar de mais contexto (ex.: rotas adicionais, uso de autenticação), peça e eu abro os arquivos relevantes.

Se algo estiver impreciso ou faltar contexto, diga qual seção prefere expandir e eu ajusto este arquivo.
