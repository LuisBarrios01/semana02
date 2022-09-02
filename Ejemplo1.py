import pandas as pd
import numpy as np

utiles = pd.Series(['Cuaderno','Lapiz',' Lapicero', 'Colores', 'Tajador', 'Borrador'],
                 index=[1,2,3,4,5,6])
print("La lista de objetos son:")
print("---------------------------")
print(utiles)

print("")

meses = pd.Series({"Enero":1, "Febrero":2, "Marzo":3, "Abril":4, "Mayo":5, "Junio":6})
print("Los 6 primeros meses son:")
print("----------------------------")
print(meses)

print("")

print("----------------------------")
numeros = pd.Series(np.random.randn(10))
print("Todos los numeros")
print(numeros)
print("")
print("Los 5 primeros numeros")
print(numeros.head(5))
print("")
print("Los ultimos 5 numeros")
print(numeros.tail(5))
print("")
print("Los 2 primeros")
print(numeros.head(2))
print("")
print("Los 2 ultimos numeros")
print(numeros.tail(2))

print("")
print("----------------------------")
ventas = {'Meses': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
          'Monto': [5000,6000,4000,8000,1000,9000]}

venta = pd.DataFrame(ventas)
print(venta)

print("")
print("Invertir cambiar las columnas")
venta1 = pd.DataFrame(ventas, columns=['Monto','Meses'])
print(venta1)

print("")
print("Leer un archivo csv")
print("")
#Convertir el archivo csv a dataFrame o Series
archivo = pd.read_csv('Ventas.csv')
archivo1 = pd.DataFrame(archivo)
print(archivo1)

print("")
print("2 listas")
#Usando la lista de ventas
ventas2021 = {'Meses': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
          'Monto': [5000,6000,4000,8000,1000,9000]}

ventas2022 = {'Meses': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
          'Monto': [4000,2000,7000,6000,3000,9000]}

venta2021 = pd.DataFrame(ventas2021)
venta2022 = pd.DataFrame(ventas2022)

datos = venta2021.add(venta2022)
print("Primera lista")
print(venta2021)
print("Segunda lista")
print(venta2022)
print("Union")
print(datos)

print("")
print("3 Primeros meses")
print("----------------------------")
data = pd.DataFrame(np.array([['Enero', 'Febrero', 'Marzo'],
                       [1000,2000,3000],
                       [4000,5000,6000],
                       [7000,8000,9000]]))

print(data)
print("")
print('filas y columnas: ', data.shape)
print('Altura: ' ,len(data.index))
print('Ancho: ' , len(data.count()))

print("")
print("Tendencia central y dispersión")
print("")
data2 = pd.DataFrame(np.array([[1000,2000,3000],
                       [4000,5000,6000],
                       [7000,8000,9000]]))

print(data2)
print("")
print(data2.describe())
print("")
print('Media: ',data2.mean())
print("")
print('Correolacion: ', data2.corr())
print("")
print('Valor bajo', data2.min())
print("")
print('Valor alto', data2.max())
print("")
print('mediana', data2.median())
print("")
print('Desviacion estandar:', data2.std())
print("")
print('Primera columna: ', data2[0])
print("")
#Se tiene que colocar dos [}
#Para columnas
print('Primera y segunda columna', data2[[0,1]])
print("")
#Iloc es para fila y columna combinar
print('Primera fila y ultima columna', data2.iloc[0][2])
print("")
#loc para filas
print('Valores de la primera fila: ', data2.loc[0])

print("")
print("Leer un archivo xlsx = excel")
#sheet_name para leer la hoja
#skiprows ignorar la primera fila
excel = pd.read_excel('Ventas02.xlsx', sheet_name='Ventas', skiprows=1)
excel1 = pd.DataFrame(excel)
print(excel1)
print("")

