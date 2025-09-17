"""
Análisis de Datos del Conjunto de Venta Minorista en Línea
Este cuaderno realiza un análisis exploratorio de datos (EDA) para un conjunto de transacciones de un minorista en línea. 
El objetivo es limpiar los datos, analizar el comportamiento de las ventas y encontrar información clave para el negocio.
Primero, importaremos las librerías necesarias:
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Configuración de visualización
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)

"""
1. Cargar y Explorar los Datos
Cargaremos el archivo CSV en un DataFrame de pandas y mostraremos la información inicial para entender su estructura."""

# Cargar el dataset
df = pd.read_csv('online_retail.csv', encoding='latin1')

# Mostrar las primeras filas del dataset
print("Primeras filas del dataset:")
print(df.head())

# Obtener información del DataFrame, incluyendo tipos de datos y valores no nulos
print("\nInformación del DataFrame:")
df.info()

"""
2. Limpieza y Preprocesamiento de Datos
Realizaremos los pasos de limpieza que discutimos para preparar el conjunto de datos para el análisis"""

# Eliminar filas con valores nulos, ya que no podemos identificar al cliente o producto
df.dropna(subset=['CustomerID', 'Description'], inplace=True)
print(f"Dataset después de eliminar valores nulos: {df.shape}")

# Eliminar transacciones donde la Cantidad o el Precio Unitario son negativos (devoluciones)
df = df[df['Quantity'] > 0]
df = df[df['UnitPrice'] > 0]
print(f"Dataset después de eliminar transacciones negativas: {df.shape}")

# Convertir la columna de la fecha a formato datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Convertir el CustomerID a un tipo de dato entero
df['CustomerID'] = df['CustomerID'].astype(int)

# Crear la columna TotalPrice para calcular el valor total de cada transacción
df['TotalPrice'] = df['Quantity'] * df['UnitPrice']

"""
3. Análisis Exploratorio de Datos (EDA)
Ahora que los datos están limpios, podemos responder a nuestras preguntas clave de negocio.

a) Los 10 Productos Más Vendidos
Calcularemos la cantidad total de unidades vendidas por cada producto para identificar los más populares.
"""
# Agrupar por 'Description' y sumar la 'Quantity'
top_selling_products = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False)

# Mostrar los 10 productos principales
print("Los 10 Productos Más Vendidos:")
print(top_selling_products.head(10))

# Visualizar los 10 productos más vendidos
plt.figure(figsize=(10, 6))
top_selling_products.head(10).sort_values().plot(kind='barh', color='skyblue')
plt.title('Top 10 Productos Más Vendidos por Cantidad')
plt.xlabel('Cantidad Total de Unidades Vendidas')
plt.ylabel('Producto')
plt.show()

""""
b) Países que Generan más Ingresos
Agruparemos los datos por país para ver la contribución de cada uno a los ingresos totales.
"""

# Agrupar por 'Country' y sumar 'TotalPrice'
country_revenue = df.groupby('Country')['TotalPrice'].sum().sort_values(ascending=False)

# Mostrar los 5 principales países por ingresos
print("Países con Más Ingresos:")
print(country_revenue.head(5))

# Visualizar los 5 países principales por ingresos
plt.figure(figsize=(10, 6))
country_revenue.head(5).sort_values().plot(kind='barh', color='lightcoral')
plt.title('Top 5 Países por Ingresos Totales')
plt.xlabel('Ingresos Totales (£)')
plt.ylabel('País')
plt.show()

""""
c) Evolución de las Ventas a lo Largo del Tiempo
Analizaremos las ventas mensuales para identificar tendencias o picos de temporada.
"""
# Configurar 'InvoiceDate' como índice y agrupar por mes
df.set_index('InvoiceDate', inplace=True)
monthly_sales = df['TotalPrice'].resample('M').sum()

# Visualizar la evolución de las ventas mensuales
plt.figure(figsize=(12, 6))
monthly_sales.plot(marker='o', linestyle='-')
plt.title('Evolución de las Ventas Totales Mensuales')
plt.xlabel('Fecha')
plt.ylabel('Ingresos Totales (£)')
plt.grid(True)
plt.show()

"""
d) Valor Medio de los Pedidos
Calcularemos el valor promedio de cada transacción para entender el gasto típico de los clientes.
"""
# Agrupar por 'InvoiceNo' para obtener el total de cada pedido y luego calcular la media
average_order_value = df.groupby('InvoiceNo')['TotalPrice'].sum().mean()

print(f"El valor medio de un pedido es de: £ {average_order_value:.2f}")

""""
Gráfico del Valor Medio de los Pedidos Mensuales
Este gráfico nos permitirá ver si el valor de las compras promedio de los clientes cambia a lo largo del año.
"""
# Restaurar la columna 'InvoiceDate' del índice al DataFrame
df.reset_index(inplace=True)

# Crear una columna con el año y el mes de cada transacción
df['YearMonth'] = df['InvoiceDate'].dt.to_period('M')

# Agrupar por 'InvoiceNo' y 'YearMonth' para calcular el valor total de cada pedido por mes
monthly_invoices = df.groupby(['InvoiceNo', 'YearMonth'])['TotalPrice'].sum().reset_index()

# Calcular el valor promedio de los pedidos para cada mes
average_monthly_order_value = monthly_invoices.groupby('YearMonth')['TotalPrice'].mean()

# Visualizar el valor promedio de los pedidos mensuales
plt.figure(figsize=(12, 6))
average_monthly_order_value.plot(kind='bar', color='darkgreen')
plt.title('Valor Medio de los Pedidos por Mes')
plt.xlabel('Mes')
plt.ylabel('Valor Medio del Pedido (£)')
plt.xticks(rotation=45)
plt.show()

"""
Interpretación del Gráfico
Este gráfico te mostrará el promedio de lo que gasta un cliente en cada pedido, mes a mes. 
Si hay picos o caídas, podría indicar temporadas en las que los clientes tienden a comprar más o menos por transacción. 
Por ejemplo, podríamos ver un aumento en noviembre y diciembre, no solo en la cantidad de pedidos, sino también en el valor de cada uno.
"""
"""
El análisis de clientes (RFM) es un excelente próximo paso para tu portafolio, ya que va más allá de las ventas generales y se enfoca en el comportamiento individual de los clientes.
Este análisis es una técnica de segmentación de mercado que utiliza tres métricas clave para identificar a los clientes más valiosos:
Recency (Recencia): ¿Hace cuánto tiempo fue la última compra de un cliente?
Frequency (Frecuencia): ¿Con qué regularidad compra un cliente?
Monetary (Valor Monetario): ¿Cuánto gasta un cliente en total?
Combinando estas métricas, podemos agrupar a los clientes en segmentos. Por ejemplo, los clientes con alta Recencia, alta Frecuencia y alto Valor Monetario son nuestros clientes más valiosos (también llamados "campeones"), mientras que aquellos con valores bajos en las tres métricas son de menor importancia.
"""
# Código para el Análisis de Clientes (RFM)
# Importar librerías necesarias
import datetime as dt

# Asegurarse de que el DataFrame no tiene el índice de fecha si se ha configurado previamente
if 'InvoiceDate' in df.index.names:
    df.reset_index(inplace=True)

# Calcular la Recencia
# La fecha más reciente de compra en el dataset es el 9 de diciembre de 2011.
# Usaremos esta fecha como referencia para calcular la recencia de cada cliente.
snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)
print(f"Fecha de referencia para el análisis de recencia: {snapshot_date}")

# Crear el DataFrame RFM
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda date: (snapshot_date - date.max()).days,
    'InvoiceNo': lambda num: num.nunique(),
    'TotalPrice': lambda price: price.sum()
})

# Renombrar las columnas para mayor claridad
rfm.columns = ['Recency', 'Frequency', 'Monetary']

# Mostrar las primeras filas del DataFrame RFM
print("\nPrimeras filas del DataFrame RFM:")
print(rfm.head())

# Describir las métricas RFM
print("\nEstadísticas descriptivas de las métricas RFM:")
print(rfm.describe())

"""
El código a continuación hace lo siguiente:
Asigna un puntaje de 1 a 4 a cada métrica.
La Recencia se puntúa de forma inversa (el puntaje más alto se da al cliente más reciente).
La Frecuencia y el Valor Monetario se puntúan de forma directa (el puntaje más alto se da al cliente con mayor valor).
Crea un "Puntaje RFM" combinando las tres métricas.
"""

# Asignar cuartiles para Recencia, Frecuencia y Valor Monetario
# Usamos 'duplicates="drop"' para manejar valores repetidos
# Creamos las etiquetas dinámicamente para que coincidan con la cantidad de bins generados
rfm['R_score'] = pd.qcut(rfm['Recency'], 4, labels=[4, 3, 2, 1], duplicates='drop')
rfm['F_score'] = pd.qcut(rfm['Frequency'], 4, labels=False, duplicates='drop') + 1
rfm['M_score'] = pd.qcut(rfm['Monetary'], 4, labels=False, duplicates='drop') + 1

# Convertir a cadena de texto para unir los puntajes
rfm['R_score'] = rfm['R_score'].astype(str)
rfm['F_score'] = rfm['F_score'].astype(str)
rfm['M_score'] = rfm['M_score'].astype(str)

# Concatenar los puntajes para crear el puntaje RFM total
rfm['RFM_Score'] = rfm['R_score'] + rfm['F_score'] + rfm['M_score']

# Mostrar el DataFrame con los nuevos puntajes
print("DataFrame con los puntajes RFM:")
print(rfm.head())

# Definir una función para asignar segmentos más robusta
def rfm_segment(row):
    r_score = int(row['R_score'])
    f_score = int(row['F_score'])
    m_score = int(row['M_score'])

    if r_score >= 3 and f_score >= 3 and m_score >= 3:
        return 'Champions'
    elif r_score >= 4 and f_score <= 2 and m_score <= 2:
        return 'New Customers'
    elif r_score >= 3 and f_score >= 3 and m_score <= 2:
        return 'Potential Loyalist'
    elif r_score <= 2 and f_score <= 2 and m_score <= 2:
        return 'Lost Customers'
    elif r_score <= 2 and f_score >= 3 and m_score >= 3:
        return 'At Risk'
    else:
        return 'Others'

# Aplicar la función para crear una nueva columna de segmentos
rfm['RFM_Segment'] = rfm.apply(rfm_segment, axis=1)

# Contar cuántos clientes hay en cada segmento y visualizar
segment_counts = rfm['RFM_Segment'].value_counts()
print("\nConteo de clientes por segmento RFM:")
print(segment_counts)

# Visualizar el conteo de clientes por segmento
plt.figure(figsize=(10, 6))
segment_counts.sort_values(ascending=False).plot(kind='bar', color='purple')
plt.title('Distribución de Clientes por Segmento RFM')
plt.xlabel('Segmento RFM')
plt.ylabel('Número de Clientes')
plt.xticks(rotation=45)
plt.show()

"""
Análisis de cestas de compra.
Este tipo de análisis nos permite encontrar reglas de asociación, como por ejemplo: 
"si un cliente compra el producto A, es probable que también compre el producto B". 
Estos patrones son muy útiles para estrategias de marketing, como recomendaciones de productos en una tienda en línea, 
colocación de productos en una tienda física, o la creación de paquetes de oferta.
"""
# Importar librerías necesarias
from mlxtend.frequent_patterns import apriori, association_rules

# Preparar los datos en el formato correcto
# Agrupar por 'InvoiceNo' y 'Description', contar la cantidad, y luego pivotar
basket = df.groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().reset_index().fillna(0).set_index('InvoiceNo')

# Convertir las cantidades a un formato booleano: True si el producto está en la cesta, False si no lo está
def encode_units_bool(x):
    return x >= 1

basket_encoded = basket.map(encode_units_bool)
# Asegurarse de que el tipo de datos sea booleano
basket_encoded = basket_encoded.astype(bool)

# Eliminar las filas de facturas canceladas para evitar errores
basket_encoded.drop('C', axis=0, errors='ignore', inplace=True)

# Aplicar el algoritmo Apriori para encontrar conjuntos de artículos frecuentes
frequent_itemsets = apriori(basket_encoded, min_support=0.01, use_colnames=True)

# Generar las reglas de asociación
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)

# Ordenar las reglas por la métrica 'lift' para ver las más interesantes
rules.sort_values('lift', ascending=False, inplace=True)

# Mostrar las 10 reglas principales
print("Reglas de Asociación principales:")
print(rules.head(10))

"""
Cada regla está compuesta por un antecedente y un consecuente, y está acompañada por métricas clave:
antecedents: Los artículos que un cliente compra primero (el "si" de la regla).
consequents: Los artículos que es probable que un cliente compre después (el "entonces" de la regla).
support (Soporte): Mide la popularidad del conjunto completo (antecedentes + consecuentes). Un soporte de 0.01 significa que el 1% de todas las transacciones contienen tanto el antecedente como el consecuente. Es un buen indicador de qué tan comunes son los artículos juntos.
confidence (Confianza): La probabilidad de que un cliente que compra el antecedente también compre el consecuente. Una confianza de 0.50 significa que el 50% de las veces que se compraron los antecedentes, también se compraron los consecuentes.
lift (Elevación): La métrica más importante. Te dice si la relación entre los productos es más fuerte de lo que se esperaría por casualidad. Un lift de 3.0 significa que la probabilidad de que los artículos se compren juntos es 3 veces mayor que la probabilidad de que se compren de forma independiente. Cualquier valor superior a 1.0 indica una relación positiva; los valores superiores a 2.0 o 3.0 son especialmente interesantes.
"""
# Código para Visualizar las Reglas de Asociación
import matplotlib.pyplot as plt

# Crear un gráfico de dispersión para visualizar las reglas
plt.figure(figsize=(10, 6))
plt.scatter(rules['support'], rules['confidence'], alpha=0.5, c=rules['lift'], cmap='viridis')
plt.colorbar(label='Lift')
plt.title('Reglas de Asociación: Support vs. Confidence')
plt.xlabel('Soporte')
plt.ylabel('Confianza')
plt.show()