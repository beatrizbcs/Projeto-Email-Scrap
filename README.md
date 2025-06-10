# Email-Scrap 📩

Este projeto automatiza o **web scraping** de uma página da web e envia os dados obtidos por **e-mail**, facilitando a coleta e o compartilhamento de informações.

## 🚀 Funcionalidades  

- **Extração de Dados**: Utiliza BeautifulSoup para coletar informações de uma página da web.  
- **Envio de E-mail**: Os dados extraídos são enviados via SMTP com Gmail.  
- **Segurança**: Armazena a senha do e-mail de forma segura usando dotenv.  

## 🛠️ Tecnologias  

- **Python**: Linguagem de programação utilizada no projeto.  
- **BeautifulSoup**: Biblioteca para extração de dados da web.  
- **SMTP**: Protocolo utilizado para envio de e-mails.  
- **dotenv**: Biblioteca para gerenciar variáveis de ambiente.  

## 📂 Estrutura do Projeto  

- **email-scrap/.env**: Armazena a senha do e-mail de forma segura.  
- **email-scrap/scraper.py**: Responsável por realizar o scraping da página.  
- **email-scrap/email_sender.py**: Envia os dados coletados por e-mail.  
- **email-scrap/main.py**: Executa todas as funcionalidades do projeto.  
- **email-scrap/requisitos.txt**: Lista as dependências necessárias para o projeto.  
- **email-scrap/README.md**: Documentação do projeto.  

## 🔧 Configuração do Arquivo `.env`  

1. **Crie um arquivo `.env`** na raiz do projeto.  
2. **Copie o conteúdo** do arquivo `.env.example` para o `.env`.  
3. **Substitua `xxxxxxxx`** pela sua senha real de e-mail.  
