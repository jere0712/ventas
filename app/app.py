import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de la página
st.set_page_config(page_title="Dashboard de Ventas - Retail", page_icon="📊", layout="wide")

# Título principal

st.title("📊🏷️ Dashboard de Análisis de Ventas")
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

#  Filtrar dataframe según selección 
df_filtrado = df[df["Category"].isin(categoria_seleccionada)]

# --- CREAR LAS PESTAÑAS ---
pestana1, pestana2 = st.tabs(["General", " Descuentos"])

# PESTAÑA 1: General

with pestana1:
    st.subheader("Indicadores Generales")
    col1, col2, col3 = st.columns(3)

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


# PESTAÑA 2: Porcentaje de Descuentos por Categoría

with pestana2:
    st.subheader("Proporción de Descuentos por Categoría")
    st.markdown("Este gráfico muestra el porcentaje relativo de transacciones con y sin descuento dentro de cada categoría.")
    
    fig_desc, ax_desc = plt.subplots(figsize=(8, 5))
    fig_desc.patch.set_alpha(0.0)
    ax_desc.patch.set_alpha(0.0)
    
    if total_transacciones > 0:
        tabla_porcentajes = pd.crosstab(df_filtrado["Category"], df_filtrado["Discount Applied"], normalize="index") * 100
        
        tabla_porcentajes.plot(kind="bar", stacked=True, ax=ax_desc, colormap="Set2")
        
        ax_desc.set_title("Distribución Porcentual de Descuentos", color="white")
        ax_desc.set_ylabel("Porcentaje (%)", color="white")
        ax_desc.set_xlabel("Categoría", color="white")
        plt.xticks(rotation=45)
        
        ax_desc.tick_params(colors='white')
        leyenda = ax_desc.legend(title="Descuento", facecolor="#1e1e1e", edgecolor="none")
        plt.setp(leyenda.get_texts(), color='white')
        plt.setp(leyenda.get_title(), color='white')
    
    st.pyplot(fig_desc, use_container_width=True)