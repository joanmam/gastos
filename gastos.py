from altres.imports import *


st.set_page_config(layout="wide")

conn = sqlitecloud.connect(cami_db)
cursor = conn.cursor()

# Carregar l'Excel en un DataFrame
df = pd.read_excel("fitxer.xlsx")

# Eliminar les primeres 5 files i les últimes 5 files
df = df.iloc[5:-5]  # Conserva totes les files excepte les primeres 5 i les últimes 5

# Opcional: guardar el DataFrame modificat a un nou fitxer
df.to_excel("fitxer_nou.xlsx", index=False)