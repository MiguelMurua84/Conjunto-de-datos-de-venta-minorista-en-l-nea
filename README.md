# 🚀 Análisis de Datos de Ventas: Un Proyecto de Data Science con Python

## Visión General del Proyecto

Este proyecto es un análisis completo de un conjunto de datos de transacciones de un minorista en línea. El objetivo es aplicar un flujo de trabajo de ciencia de datos, desde la limpieza de datos hasta la obtención de información de negocio clave, para ayudar a la empresa a tomar decisiones informadas sobre productos, marketing y relaciones con los clientes.

El análisis está disponible en el archivo `analisis_ventas_online.py`.

## Conjunto de Datos

El conjunto de datos utilizado es `online_retail.csv`, que contiene transacciones de un minorista en línea de Reino Unido entre 2010 y 2011.

**Columnas principales:**
* `InvoiceNo`: Número de factura.
* `StockCode`: Código del producto.
* `Description`: Nombre del producto.
* `Quantity`: Cantidad de productos en la transacción.
* `InvoiceDate`: Fecha de la transacción.
* `UnitPrice`: Precio unitario del producto.
* `CustomerID`: Identificador del cliente.
* `Country`: País de residencia del cliente.

## Pasos del Análisis

### 1. Limpieza y Preprocesamiento de Datos

* Se manejaron valores faltantes en las columnas `CustomerID` y `Description`.
* Se eliminaron transacciones con valores negativos en `Quantity` y `UnitPrice`, que representan devoluciones o cancelaciones.
* Se creó una nueva columna, `TotalPrice`, para calcular el valor total de cada transacción.

### 2. Análisis Exploratorio de Datos (EDA)

Se realizó un análisis para entender las características clave del negocio, respondiendo a las siguientes preguntas:

* **Productos más vendidos:** Identificación de los 10 productos más populares.
* **Ingresos por país:** Descubrimiento de los mercados más rentables, con un claro liderazgo del Reino Unido.
* **Tendencias de ventas:** Se visualizó el crecimiento de las ventas a lo largo del tiempo, con un pico significativo en la temporada navideña de 2011.
[Aquí puedes insertar un gráfico de ventas mensuales]

### 3. Análisis de Clientes (RFM)

Se segmentó a los clientes utilizando el modelo RFM (Recencia, Frecuencia y Valor Monetario) para identificar a los clientes más valiosos y a aquellos en riesgo.

* **Segmentos clave:** Se identificaron grupos como "Champions" (clientes más valiosos) y "Lost Customers" (clientes perdidos), lo que permite estrategias de marketing personalizadas.
[Aquí puedes insertar un gráfico de distribución de clientes por segmento]

### 4. Análisis de Cestas de Compra

Se utilizaron reglas de asociación para encontrar productos que se compran juntos con frecuencia, proporcionando información valiosa para:

* **Recomendaciones de productos:** Sugerir artículos complementarios a los clientes.
* **Estrategias de ventas:** Crear paquetes de productos para aumentar el valor promedio de los pedidos.
[Aquí puedes insertar el gráfico de dispersión de las reglas de asociación]

## Conclusiones

Este proyecto demuestra la capacidad para realizar un análisis de datos de extremo a extremo, transformando datos sin procesar en conocimiento accionable. Las conclusiones obtenidas pueden usarse para mejorar la gestión de inventario, optimizar las campañas de marketing y fortalecer la retención de clientes.

## Tecnologías y Librerías

* **Lenguaje de Programación:** Python
* **Análisis de Datos:** `pandas`, `numpy`
* **Visualización:** `matplotlib`, `seaborn`
* **Algoritmos:** `mlxtend` (para reglas de asociación)

## Imagenes

<img width="1920" height="967" alt="Distribución de clientes por segmento RFm" src="https://github.com/user-attachments/assets/719cc13e-22ae-498c-a33c-d7717ca488e4" />
<img width="1920" height="967" alt="Evolucion de las ventas totales mensuales" src="https://github.com/user-attachments/assets/5a19458f-3687-429a-bc70-2d78dd1550e3" />
<img width="1920" height="967" alt="Reglas de Asociación Support vs  Confidence" src="https://github.com/user-attachments/assets/a9092705-791f-4a1f-80e5-0bc2fc9d6856" />
<img width="1920" height="967" alt="Top 5 países por ingresos totatelas" src="https://github.com/user-attachments/assets/009f0902-5fdf-45cf-91aa-26be011a7423" />
<img width="1920" height="967" alt="Top 10 productos más vendidos por cantidad" src="https://github.com/user-attachments/assets/caae7eb8-da95-4cf7-9c1c-fad4296c85e3" />
<img width="1920" height="967" alt="Valor medio de los pedidos por mes" src="https://github.com/user-attachments/assets/e9cc8f3e-0c94-4d09-b504-af4dea755235" />


## Autor

Miguel Murua
https://www.linkedin.com/in/miguelmurua/
