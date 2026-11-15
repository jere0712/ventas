# Análisis de datos en el comercio

## 📋 Introducción
El análisis de datos en el comercio minorista (retail) es fundamental para comprender la dinámica del mercado y el comportamiento de los consumidores. Ante el volumen masivo de registros transaccionales presenciales y digitales, las empresas requieren metodologías estadísticas precisas para optimizar sus operaciones. Este informe se estructura para dar respuesta a interrogantes clave sobre las ventas minoristas. Comienza con el Planteamiento del Problema (justificación, objetivos, cobertura y definición de variables). Posteriormente, aborda la limpieza de datos, el análisis estadístico descriptivo para resolver las preguntas de investigación y la generación de visualizaciones integradas. Todo el desarrollo se ejecuta bajo un enfoque de reproducibilidad mediante un documento dinámico en RMarkdown.

---

## 🎯 Planteamiento del Problema
El sector del comercio al por menor (retail) opera en un entorno altamente dinámico y competitivo, donde la gestión eficiente de las transacciones comerciales, la comprensión de los patrones de consumo y la optimización de los canales de venta (físico y digital) resultan fundamentales para la sostenibilidad financiera de los establecimientos. La irrupción de nuevas modalidades de pago, como las billeteras digitales y tarjetas, combinada con políticas de descuentos dinámicos y la diversificación de categorías de productos, genera un volumen masivo de datos transaccionales que requieren un tratamiento analítico riguroso.

---

## 💡 Justificación
La presente investigación se justifica en la necesidad de dotar a la gestión comercial minorista de herramientas estadísticas objetivas y reproducibles. A nivel práctico, el análisis detallado de las transacciones correspondientes al periodo 2022-2025 permitirá optimizar las estrategias de precios, la segmentación de clientes y la asignación de recursos operativos entre los canales digitales y físicos. Desde una perspectiva metodológica, el estudio establece un flujo de trabajo reproducible basado en programación estadística, garantizando la trazabilidad, la precisión y la transparencia en el tratamiento de los datos. Esto aporta valor estratégico a la organización y consolida un marco de aplicación directa para la analítica empresarial en el ámbito académico.

---

## 🎯 Objetivos

### Objetivo General
Analizar integralmente el rendimiento comercial minorista a través del procesamiento estadístico del histórico transaccional 2022-2025, mediante el uso de herramientas computacionales en R, para optimizar la toma de decisiones estratégicas basadas en el comportamiento del consumidor.

### Objetivos Específicos
1. Caracterizar la distribución univariada y multivariada de las variables cuantitativas (precios unitarios, cantidades y montos totales) y cualitativas (categorías, ubicación y métodos de pago).
2. Evaluar el impacto de la aplicación de descuentos y los canales de compra (Online frente a In-store) sobre el gasto total de los clientes.
3. Desarrollar un flujo de trabajo reproducible e integrado en RMarkdown con salida en HTML que garantice la trazabilidad y transparencia de todo el análisis estadístico.
4. Identificar las categorías de productos y los periodos temporales donde se concentra con mayor frecuencia la aplicación de políticas de descuentos.

---

## 📂 Estructura del Informe
El informe y el repositorio se estructuran de la siguiente manera:
1. **Introducción y Objetivos:** Contextualización del estudio y preguntas de investigación.
2. **Metodología y Limpieza de Datos:** Carga, depuración y tratamiento de valores perdidos (imputación por mediana) para garantizar la integridad de las 12,575 observaciones.
3. **Análisis Principal (Descuentos y Ventas):** Evaluación del impacto del descuento sobre el monto gastado (`total_spent`) y las unidades adquiridas (`quantity`), apoyado en medidas de tendencia central y gráficos de cajas (*boxplots*).
4. **Análisis Cruzado:** Segmentación del comportamiento según categorías de productos, canales de venta y métodos de pago (*Cash, Credit Card, Digital Wallet*).
5. **Conclusiones y Recomendaciones:** Hallazgos analíticos clave orientados a la toma de decisiones comerciales.

---

## 👥 Equipo de Trabajo y Reproducibilidad
El proyecto ha sido desarrollado de forma colaborativa mediante control de versiones en **GitHub** y procesamiento en entorno **RMarkdown** (`informe.Rmd`), garantizando la trazabilidad, transparencia y actualización periódica de los resultados gerenciales.