# Teste Técnico – Web Scraping e Transformação de Dados | Intuitive Care

Este projeto foi desenvolvido como parte de um teste técnico para vaga de estágio na Intuitive Care.

Ele inclui dois testes:

- **Teste 1 – Web Scraping**
- **Teste 2 – Transformação de Dados**

---

## Teste 1 – Web Scraping

O script realiza automaticamente o download dos arquivos "Anexo I" e "Anexo II" do site oficial da ANS e os compacta diretamente em um arquivo `.zip`.

### O que o script faz:
✔️ Acessa a página da ANS  
✔️ Encontra os links dos PDFs “Anexo I” e “Anexo II”  
✔️ Baixa os arquivos automaticamente  
✔️ Cria um arquivo `anexos.zip` contendo os dois documentos, sem deixar os PDFs soltos

---

## Teste 2 – Transformação de Dados

Utiliza o arquivo `Anexo_1.pdf`, extraído do `anexos.zip`, para:

✔️ Extrair a tabela “Rol de Procedimentos e Eventos em Saúde”  
✔️ Juntar todas as páginas em um único DataFrame  
✔️ Substituir as siglas `OD` e `AMB` por descrições completas (com base na legenda)  
✔️ Salvar a tabela como CSV  
✔️ Compactar o resultado em um arquivo chamado `Teste_Gessyca.zip`

---

## Requisitos

- Python 3.8 ou superior  
- Git instalado (ou baixe o projeto em `.zip`)  
- Conexão com a internet  
- Ambiente de testes: **Windows 11**

---

## Como testar o projeto:

### 1. Clone este repositório:

``git clone https://github.com/seu-usuario/teste-nivelamento-intuitive-care.git``

### 2. Navegue até a pasta do projeto:

``cd teste-nivelamento-intuitive-care/web-scraping-tranformacao``

### 3. Crie o ambiente virtual:

``python -m venv venv``

### 4. Ative o ambiente virtual:

``venv\Scripts\activate``

### 5. Instale as dependências:

``pip install -r requirements.txt``

Se não tiver um ``requirements.txt``, instale manualmente:

``pip install requests beautifulsoup4 pdfplumber pandas``

### 6. Execute o Teste 1 (Web Scraping):

``python main.py``

Isso irá gerar o arquivo:

``anexos.zip``

### 7. Execute o Teste 2 (Transformação de Dados):

``python transformacao.py``

O script irá:

✔️ Extrair o Anexo_1.pdf do anexos.zip

✔️ Processar todas as páginas

✔️ Gerar um arquivo final chamado:

``Teste_Gessyca.zip``




