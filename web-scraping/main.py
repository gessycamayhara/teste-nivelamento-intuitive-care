import requests
from bs4 import BeautifulSoup
from zipfile import ZipFile

# Acessar a página da ANS
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Encontrar os links dos PDFs com "Anexo I" e "Anexo II"
pdf_links = []
for link in soup.find_all("a", href=True):
    texto = link.get_text().lower()
    href = link["href"]
    if ("anexo i" in texto or "anexo ii" in texto) and href.endswith(".pdf"):
        if href.startswith("/"):
            href = "https://www.gov.br" + href
        pdf_links.append(href)

# Criar o arquivo ZIP e adicionar os PDFs direto nele
with ZipFile("anexos.zip", "w") as zipf:
    for i, pdf_url in enumerate(pdf_links, start=1):
        nome_arquivo = f"Anexo_{i}.pdf"
        print(f"Baixando {nome_arquivo} de {pdf_url}...")
        r = requests.get(pdf_url)
        zipf.writestr(nome_arquivo, r.content)
        print(f"Adicionado {nome_arquivo} ao ZIP.")

print("Processo concluído!")