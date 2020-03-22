import numpy as np
import scipy as misc
import pandas as pd
import matplotlib.pyplot as plt
import random

# FILTERED_REGIONS = ["Abruzzo", "Basilicata", "P.A. Bolzano", "Calabria", "Campania", "Emilia Romagna", "Friuli Venezia Giulia", "Lazio", "Liguria", "Lombardia", "Marche", "Molise", "Piemonte", "Puglia", "Sardegna", "Sicilia", "Toscana", "P.A. Trento", "Umbria", "Valle d'Aosta", "Veneto"]
FILTERED_REGIONS = ["Emilia Romagna", "Lazio", "Lombardia", "Piemonte", "Puglia", "Toscana", "Veneto"]

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
df = df.filter(["data", "denominazione_regione", "totale_attualmente_positivi"])
df["day"] = -1

# Clean date
df["data"] = df["data"].apply(convertData)
# Start where there are at least 100 cases
df = df[df["totale_attualmente_positivi"] > 99]
df = df[df["denominazione_regione"].isin(FILTERED_REGIONS)]

# df.plot(x = "data", y = "totale_attualmente_positivi", kind = "scatter")
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

  # regions_data[region].plot(x = "day", y = "totale_attualmente_positivi")
  plt.plot("day", "totale_attualmente_positivi", label=region, data=regions_data[region], markersize=2, color=randColor(), linewidth=2)


# regions_data["Veneto"].plot(x = "day", y = "totale_attualmente_positivi", kind = "scatter")
# plt.show()

# italy = pd.concat(regions_list, axis=0)
# italy.plot(x = "day", y = "totale_attualmente_positivi") #, kind = "scatter")
plt.legend(loc='upper center', shadow=True, ncol=2)
plt.show()

# printRegions(FILTERED_REGIONS, regions_data)
