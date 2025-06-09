Email-Scrap 📩
Este projeto automatiza o web scraping de uma página da web e envia os dados coletados por e-mail, facilitando a obtenção e o compartilhamento de informações.

🚀 Funcionalidades
Extrai dados de uma página usando BeautifulSoup.

Envia os dados coletados via SMTP com Gmail.

Armazena a senha do e-mail de forma segura com dotenv.

🛠️ Tecnologias
Python

BeautifulSoup

SMTP (para envio de e-mails)

dotenv (para variáveis de ambiente)

📂 Estrutura do projeto
email-scrap/
│── .env  # Armazena a senha do e-mail
│── scraper.py  # Faz o scraping da página
│── email_sender.py  # Envia os dados por e-mail
│── main.py  # Executa tudo junto
│── requirements.txt  # Dependências do projeto
│── README.md  # Documentação do projeto

🔧 Configuração do arquivo .env
- Crie um arquivo `.env` na raiz do projeto.
- Copie o conteúdo do `.env.example` para o `.env`.
- Substitua `xxxxxxxx` pela sua senha real de e-mail.