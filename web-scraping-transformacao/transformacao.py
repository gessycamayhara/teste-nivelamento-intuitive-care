import pdfplumber
import pandas as pd
from zipfile import ZipFile
import os

# Caminho do ZIP e nome do PDF dentro dele
zip_path = "anexos.zip"
pdf_filename = "Anexo_1.pdf"

# Extrair o PDF do ZIP
if not os.path.exists(pdf_filename):
    print(f"Extraindo {pdf_filename} de {zip_path}...")
    with ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extract(pdf_filename)
    print("Extração concluída.\n")


tabelas = []

# Abrir o PDF e extrair tabelas
with pdfplumber.open(pdf_filename) as pdf:
    for i, pagina in enumerate(pdf.pages, start=1):
        print(f"Extraindo página {i}...")
        try:
            tabelas_da_pagina = pagina.extract_tables()
            for tabela in tabelas_da_pagina:
                if tabela:
                    df = pd.DataFrame(tabela[1:], columns=tabela[0])
                    tabelas.append(df)
        except Exception as e:
            print(f"Erro ao processar a página {i}: {e}")

# Verificar se alguma tabela foi extraída
if not tabelas:
    print("\n Nenhuma tabela foi extraída do PDF.")
else:
    
    df_total = pd.concat(tabelas, ignore_index=True)
    print(f"\n Total de tabelas extraídas: {len(tabelas)}")
    print("\n Primeiras linhas da tabela combinada:")
    print(df_total.head())

# Substituir siglas nas colunas OD e AMB
substituicoes = {
    "OD": "Consulta com cirurgião-dentista",  # ajuste com base no PDF
    "AMB": "Atendimento ambulatorial"
}

colunas_para_substituir = ["OD", "AMB"]
for coluna in colunas_para_substituir:
    if coluna in df_total.columns:
        df_total[coluna] = df_total[coluna].replace(substituicoes)

# Salvar como CSV
csv_nome = "rol_procedimentos.csv"
df_total.to_csv(csv_nome, index=False)
print(f"\nCSV salvo como: {csv_nome}")

# Compactar o CSV em um arquivo .zip
zip_nome = "Teste_Gessyca.zip"
with ZipFile(zip_nome, "w") as zipf:
    zipf.write(csv_nome)
print(f"Arquivo compactado gerado: {zip_nome}")

os.remove(csv_nome)
print(f"CSV removido da pasta. Apenas {zip_nome} permanece.")
