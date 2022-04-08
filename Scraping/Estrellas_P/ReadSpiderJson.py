import json
import pandas as pd
import os
daj = open('Estrellas20220223.json',)

data = json.load(daj)
data = data[0]

daj.close()

#print(type(data))
#print(data['Nombre'])
#print(" ".join(data['Nombre'][2].split()))
##
Rank = data['Rank']
RankTop5 = Rank[0:5]
print(len(RankTop5))
print(RankTop5)

Nombre = data['Nombre']
Nombre = [" ".join(i.split()) for i in Nombre]
Nombre = [i for i in Nombre if len(i) > 1]
NombreTop5 = Nombre[0:5]
print(len(NombreTop5))
print(NombreTop5)

Apellido = data['Apellido']
ApellidoTop5 = Apellido[0:5]
print(len(ApellidoTop5))
print(ApellidoTop5)

Info = data['Info']
Info = [" ".join(i.split()) for i in Info]
InfoTop5 = Info[0:5]
print(len(InfoTop5))
print(InfoTop5)

photo = data['photo']
photo = [" ".join(i.split()) for i in photo]
photoTop5 = photo[0:5]
print(len(photoTop5))
print(photoTop5)

Estrellas = [RankTop5, NombreTop5, ApellidoTop5, InfoTop5, photoTop5]

Estrellas = pd.DataFrame(Estrellas, index=['Rank', 'Nombre', 'Apellido', 'Info', 'photo']).T
Estrellas['Fecha'] = '20220223'
print(Estrellas)

#Estrellas.to_excel('Base_Estrellas.xlsx')
Estrellastemp = pd.read_excel('Base_Estrellas.xlsx', index_col = 0)
Tabla_Excel = pd.concat([Estrellastemp, Estrellas], sort = False)
Tabla_Excel.to_excel("Base_Estrellas.xlsx")

os.remove("Estrellas20220223.json") 