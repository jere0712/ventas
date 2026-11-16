import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title="Dashboard de Ventas - Retail", page_icon="📊", layout="wide")

# Título principal

st.title("📊 Dashboard de Análisis de Ventas Retail")
st.markdown("Visualización interactiva del comportamiento de compra, descuentos y canales.")

# Cargar la base de datos (asegúrate de que el archivo CSV esté en la misma carpeta)
@st.cache_data
def cargar_datos():
    df = pd.read_csv("app/retail_store_sales.csv")
    return df

df = cargar_datos()

# --- FILTROS LATERALES ---
st.sidebar.header("Filtros de Visualización")
categoria_seleccionada = st.sidebar.multiselect(
    "Selecciona la Categoría:",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

# Filtrar dataframe según selección
df_filtrado = df[df["Category"].isin(categoria_seleccionada)]

# --- MÉTRICAS PRINCIPALES (KPIs) ---
st.subheader("Indicadores Generales")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Total de Transacciones", value=len(df_filtrado))
with col2:
    gasto_promedio = df_filtrado["Total Spent"].mean()
    st.metric(label="Gasto Promedio (Ticket)", value=f"${gasto_promedio:.2f}")
with col3:
    cantidad_promedio = df_filtrado["Quantity"].mean()
    st.metric(label="Cantidad Promedio", value=f"{cantidad_promedio:.1f} unidades")

st.divider()

# --- GRÁFICOS ---
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("Gasto Total según Descuento")
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.boxplot(data=df_filtrado, x="Discount Applied", y="Total Spent", palette=["#C62828", "#2E7D32"], ax=ax)
    ax.set_title("Distribución del Gasto Total")
    st.pyplot(fig)

with col_graf2:
    st.subheader("Ventas por Categoría")
    ventas_cat = df_filtrado.groupby("Category")["Total Spent"].sum().reset_index()
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(data=ventas_cat, x="Category", y="Total Spent", palette="Blues_d", ax=ax)
    plt.xticks(rotation=45)
    ax.set_title("Ingresos Totales por Categoría")
    st.pyplot(fig)