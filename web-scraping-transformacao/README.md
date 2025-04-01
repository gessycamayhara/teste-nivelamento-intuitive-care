## Teste Técnico – Web Scraping | Intuitive Care

Este projeto foi desenvolvido como parte de um teste técnico para vaga de estágio na Intuitive Care.

Ele realiza automaticamente o download dos arquivos **"Anexo I"** e **"Anexo II"** do site oficial da ANS e os compacta diretamente em um arquivo `.zip`.

---

## O que o script faz:

✔️ Acessa a página da ANS  
✔️ Encontra os links dos PDFs “Anexo I” e “Anexo II”  
✔️ Baixa os arquivos automaticamente  
✔️ Cria um arquivo `anexos.zip` contendo os dois documentos, sem deixar os PDFs soltos

---

## Requisitos:

- Python 3.8 ou superior
- Git instalado (ou baixe o projeto em .zip)
- Conexão com a internet
- Ambiente de testes: **Windows 11**

---

## Como testar o projeto 

### 1. Clone este repositório:

Via terminal:

`git clone https://github.com/seu-usuario/teste-nivelamento.git`

### 2. Navegue até a pasta do projeto:

`cd teste-nivelamento/web-scraping`

### 3. Crie o ambiente virtual:

`python -m venv venv`

### 4. Ative o ambiente virtual:

`venv\Scripts\activate`

### 5. Instale as dependências:

`pip install -r requirements.txt`

Se você não tiver um requirements.txt, instale diretamente:

`pip install requests beautifulsoup4`

### 6. Execute o script:

`python main.py`

