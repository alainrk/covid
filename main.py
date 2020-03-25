import numpy as np
import scipy as misc
import pandas as pd
import matplotlib.pyplot as plt
import random

# FILTERED_REGIONS = ["Abruzzo", "Basilicata", "P.A. Bolzano", "Calabria", "Campania", "Emilia Romagna", "Friuli Venezia Giulia", "Lazio", "Liguria", "Lombardia", "Marche", "Molise", "Piemonte", "Puglia", "Sardegna", "Sicilia", "Toscana", "P.A. Trento", "Umbria", "Valle d'Aosta", "Veneto"]
FILTERED_REGIONS = ["Emilia Romagna", "Lazio", "Lombardia", "Piemonte", "Puglia", "Toscana", "Veneto"]
COLORS = { "Emilia Romagna": "green", "Lazio": "red", "Lombardia": "blue", "Piemonte": "brown", "Puglia": "orange", "Toscana": "purple", "Veneto": "black" }

def randColor():
  return (random.random(), random.random(), random.random(), 1)

def convertData(d):
  return d.split(" ")[0]

def printRegions(regions, regions_data):
  for region in regions:
    print(regions_data[region].head(), '\n\n')

# Useful columns
# data,denominazione_regione,ricoverati_con_sintomi,terapia_intensiva,totale_ospedalizzati,isolamento_domiciliare,totale_attualmente_positivi,nuovi_attualmente_positivi,dimessi_guariti,deceduti,totale_casi,tamponi

# df = pd.read_csv("data.csv", sep="," , header=None)
df = pd.read_csv("data.csv")
df = df.filter(["data", "denominazione_regione", "totale_casi", "terapia_intensiva", "nuovi_attualmente_positivi", "deceduti"])
df["day"] = -1

# Clean date
df["data"] = df["data"].apply(convertData)
# Start where there are at least 100 cases
df = df[df["totale_casi"] > 99]
df = df[df["denominazione_regione"].isin(FILTERED_REGIONS)]

# df.plot(x = "data", y = "totale_casi", kind = "scatter")
# plt.show()

regions_data = {}
regions_list = []
for region in FILTERED_REGIONS:
  regions_data[region] = df[df["denominazione_regione"] == region]
  # tmp = df[df["denominazione_regione"] == region]
  # regions_data[region] = tmp.copy()
  regions_list.append(regions_data[region])

  count = 0
  for index, row in regions_data[region].iterrows():
    regions_data[region].at[index, "day"] = count
    count += 1

  # regions_data[region].plot(x = "day", y = "totale_casi")
  plt.plot("day", "totale_casi", label=region, data=regions_data[region], markersize=2, color=COLORS[region], linewidth=2)
  # plt.plot("day", "terapia_intensiva", label=region, data=regions_data[region], markersize=2, color=COLORS[region], linewidth=2)
  # plt.plot("day", "nuovi_attualmente_positivi", label=region, data=regions_data[region], markersize=2, color=COLORS[region], linewidth=2)
  # plt.plot("day", "deceduti", label=region, data=regions_data[region], markersize=2, color=COLORS[region], linewidth=2)


# regions_data["Veneto"].plot(x = "day", y = "totale_casi", kind = "scatter")
# plt.show()

# italy = pd.concat(regions_list, axis=0)
# italy.plot(x = "day", y = "totale_casi") #, kind = "scatter")
plt.legend(loc='upper center', shadow=True, ncol=2)
plt.title('Totale casi')
# plt.title('Terapia intensiva')
# plt.title('Nuovi casi')
# plt.title('Deceduti')
plt.show()

# printRegions(FILTERED_REGIONS, regions_data)
