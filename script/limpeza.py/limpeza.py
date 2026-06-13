import pandas as pd

# 1. Carregar os dados brutos da pasta raw
caminho_arquivo_bruto = 'data/raw/netflix_data_history.csv'
df = pd.read_csv(caminho_arquivo_bruto)

# 2. Exploração rápida no terminal para verificar a saúde dos dados
print("--- Amostragem dos Dados Brutos ---")
print(df.head())
print("\n--- Informações das Colunas e Nulos ---")
print(df.info())

# 3. Limpeza e Tratamento (Data Cleaning)
# Remover linhas que contenham valores vazios/nulos
df = df.dropna()

# Converter a coluna de data para o tipo datetime (Crucial para o Power BI criar hierarquias de tempo)
# Nota: Verifique se no seu CSV a coluna chama-se 'Date'. Se for diferente, ajuste o nome entre aspas.
df['Date'] = pd.to_datetime(df['Date'])

# Remover possíveis linhas duplicadas
df = df.drop_duplicates()

# 4. Salvar o arquivo tratado na pasta processed
caminho_arquivo_processado = 'data/processed/netflix_dados_limpos.csv'
df.to_csv(caminho_arquivo_processado, index=False)

print(f"\n🎉 Sucesso! Arquivo limpo salvo em: {caminho_arquivo_processado}")