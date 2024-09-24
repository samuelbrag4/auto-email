# 📧 Email Automático com Python

Este projeto tem como objetivo automatizar o envio de respostas para e-mails específicos utilizando **Python** e as bibliotecas `imaplib` e `smtplib`. O script verifica sua caixa de entrada em intervalos de tempo e envia respostas automáticas para determinados remetentes.

---

## 🛠 Funcionalidades

- 📬 Verifica automaticamente a caixa de entrada do Gmail a cada 1 minuto.
- 📋 Filtra e-mails de remetentes específicos e responde apenas a esses remetentes.
- ✉️ Envia uma resposta automática personalizada confirmando o recebimento do e-mail.

---

## 🚀 Tecnologias Utilizadas

- **Python**: Linguagem de programação utilizada para automação.
- **imaplib**: Para acessar a caixa de entrada e buscar e-mails não lidos.
- **smtplib**: Para enviar e-mails automáticos.
- **email.mime**: Para estruturar o corpo e assunto do e-mail.
- **time**: Para controlar o intervalo de verificação de e-mails.
- **os**: Para acessar variáveis de ambiente e manter as credenciais seguras.

---

## 🔧 Instalação e Configuração

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
