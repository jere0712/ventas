import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title="Dashboard de Ventas - Retail", page_icon="📊", layout="wide")

# Título principal

st.title("📊 Dashboard de Análisis de Ventas")
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

# --- MÉTRICAS PRINCIPALES (KPIS) ---
st.subheader("Indicadores Generales")
col1, col2, col3 = st.columns(3)

# Evitar errores de división o NaN si no hay datos seleccionados
total_transacciones = len(df_filtrado)

if total_transacciones > 0:
    gasto_promedio = df_filtrado["Total Spent"].mean()
    cantidad_promedio = df_filtrado["Quantity"].mean()
else:
    gasto_promedio = 0.0
    cantidad_promedio = 0.0

with col1:
    st.metric(label="Total de Transacciones", value=total_transacciones)
with col2:
    st.metric(label="Gasto Promedio (Ticket)", value=f"${gasto_promedio:.2f}")
with col3:
    st.metric(label="Cantidad Promedio", value=f"{cantidad_promedio:.1f} unidades")

st.divider()

# --- GRÁFICOS ---
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("Gasto Total según Descuento")
    fig, ax = plt.subplots(figsize=(6, 4))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    
    if total_transacciones > 0:
        sns.boxplot(data=df_filtrado, x="Discount Applied", y="Total Spent", palette=["#C62828", "#2E7D32"], ax=ax)
    
    ax.set_title("Distribución del Gasto Total", color="white")
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    st.pyplot(fig, use_container_width=True)

with col_graf2:
    st.subheader("Ventas por Categoría")
    fig, ax = plt.subplots(figsize=(6, 4))
    fig.patch.set_alpha(0.0)
    ax.patch.set_alpha(0.0)
    
    if total_transacciones > 0:
        ventas_cat = df_filtrado.groupby("Category")["Total Spent"].sum().reset_index()
        sns.barplot(data=ventas_cat, x="Category", y="Total Spent", palette="Blues_d", ax=ax)
        plt.xticks(rotation=45)
        
    ax.set_title("Ingresos Totales por Categoría", color="white")
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    st.pyplot(fig, use_container_width=True)