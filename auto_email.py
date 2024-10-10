import imaplib  # Acessa sua caixa de entrada via IMAP
import smtplib  # Envia e-mails via SMTP
from email.mime.text import MIMEText  # Cria o corpo do e-mail
from email.mime.multipart import MIMEMultipart  # Cria um e-mail com múltiplos componentes
import email  # Manipula e-mails recebidos
import time  # Pausa a execução do código (usado para verificar e-mails em intervalos)
import os  # Para acessar as variáveis de ambiente

# Configurações do e-mail (usando variáveis de ambiente)
email_de = os.getenv("EMAIL_USUARIO")  # Variável de ambiente para o e-mail
senha = os.getenv("EMAIL_SENHA")  # Variável de ambiente para a senha de app gerada

# Lista de e-mails permitidos para receber a resposta automática (exemplo dos seus professores)
emails_permitidos = [
    "fulanodetal@gmail.com"
]

# Função para enviar uma resposta automática ao remetente
def enviar_resposta(remetente):
    mensagem = MIMEMultipart()
    mensagem["From"] = email_de
    mensagem["To"] = remetente
    mensagem["Subject"] = "Confirmação de Recebimento de e-mail"

    corpo = "Seu e-mail foi recebido! Logo logo te respondo 😉"
    mensagem.attach(MIMEText(corpo, "plain"))

    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(email_de, senha)
    servidor.sendmail(email_de, remetente, mensagem.as_string())
    servidor.quit()

    print(f"Resposta automática enviada para {remetente}")

# Função para verificar novos e-mails não lidos e responder se o remetente estiver na lista
def verificar_e_responder():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(email_de, senha)
    mail.select("inbox")

    status, dados = mail.search(None, 'UNSEEN')  # Buscar e-mails não lidos (flag UNSEEN)
    emails_nao_lidos = dados[0].split()

    for num in emails_nao_lidos:
        status, dados = mail.fetch(num, '(RFC822)')
        mensagem_email = email.message_from_bytes(dados[0][1])
        remetente = email.utils.parseaddr(mensagem_email["From"])[1]  # Extrair o endereço do remetente

        # Verificar se o remetente está na lista de e-mails permitidos
        if remetente in emails_permitidos:
            enviar_resposta(remetente)  # Enviar resposta automática se o e-mail for de um professor
        else:
            print(f"E-mail de {remetente} não está na lista permitida. Nenhuma resposta enviada.")

    mail.logout()

# Loop infinito para verificar e-mails a cada 1 minuto
while True:
    verificar_e_responder()  # Verificar e-mails e responder automaticamente
    time.sleep(60)  # Pausar por 1 minuto antes de verificar novamente