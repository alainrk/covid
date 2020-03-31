import numpy as np
import scipy as misc
import pandas as pd
import matplotlib.pyplot as plt
import random
from datetime import datetime
from scipy.optimize import curve_fit

# FILTERED_REGIONS = ["Abruzzo", "Basilicata", "P.A. Bolzano", "Calabria", "Campania", "Emilia Romagna", "Friuli Venezia Giulia", "Lazio", "Liguria", "Lombardia", "Marche", "Molise", "Piemonte", "Puglia", "Sardegna", "Sicilia", "Toscana", "P.A. Trento", "Umbria", "Valle d'Aosta", "Veneto"]
# FILTERED_REGIONS = ["Italia"]
FILTERED_REGIONS = ["Italia", "Emilia Romagna", "Lombardia", "Piemonte", "Veneto"]

COLORS = { "Emilia Romagna": "green", "Lazio": "magenta", "Lombardia": "blue", "Piemonte": "red", "Puglia": "pink", "Toscana": "purple", "Veneto": "orange", "Italia": "black" }

def randColor():
  return (random.random(), random.random(), random.random(), 1)

def getColor(region):
  if region in COLORS:
    return COLORS[region]
  return randColor()

def setColors():
  for region in FILTERED_REGIONS:
    if region not in COLORS:
      COLORS[region] = randColor()

def convertData(d):
  return d.split("T")[0]
  # return d.split("T")[0]

def printRegions(regions, regions_data):
  for region in regions:
    print(regions_data[region].head(), '\n\n')

setColors()

# Useful columns
# data,denominazione_regione,ricoverati_con_sintomi,terapia_intensiva,totale_ospedalizzati,isolamento_domiciliare,totale_attualmente_positivi,nuovi_attualmente_positivi,dimessi_guariti,deceduti,totale_casi,tamponi

df_it = pd.read_csv("italia.csv")
df_it = df_it.filter(["data", "denominazione_regione", "totale_casi", "terapia_intensiva", "nuovi_attualmente_positivi", "deceduti", "totale_attualmente_positivi"])
df_it["day"] = -1
df_it["denominazione_regione"] = "Italia"

df_reg = pd.read_csv("regioni.csv")
df_reg = df_reg.filter(["data", "denominazione_regione", "totale_casi", "terapia_intensiva", "nuovi_attualmente_positivi", "deceduti", "totale_attualmente_positivi"])
df_reg["day"] = -1

frames = [df_it, df_reg]
df = pd.concat(frames)

# Clean date
df["data"] = df["data"].apply(convertData)
# Start where there are at least 100 cases
df = df[df["totale_casi"] > 99]
df = df[df["denominazione_regione"].isin(FILTERED_REGIONS)]

fig, axs = plt.subplots(3, 2)

regions_data = {}
regions_list = []
for region in FILTERED_REGIONS:
  regions_data[region] = df[df["denominazione_regione"] == region].copy(True)
  # regions_data[region].index = range(regions_data[region].size)

  regions_data[region]["totale_casi_ieri"] = regions_data[region]["totale_casi"].shift(1)
  today = regions_data[region]["totale_casi"]
  yesterday = regions_data[region]["totale_casi_ieri"]
  # regions_data[region]["delta_totale"] = (today - yesterday) / yesterday * 100
  regions_data[region]["delta_totale"] = (today - yesterday)

  regions_data[region]["terapia_intensiva_ieri"] = regions_data[region]["terapia_intensiva"].shift(1)
  today = regions_data[region]["terapia_intensiva"]
  yesterday = regions_data[region]["terapia_intensiva_ieri"]
  # regions_data[region]["delta_terapia_intensiva"] = (today - yesterday) / yesterday * 100
  regions_data[region]["delta_terapia_intensiva"] = (today - yesterday)

  regions_data[region]["deceduti_ieri"] = regions_data[region]["deceduti"].shift(1)
  today = regions_data[region]["deceduti"]
  yesterday = regions_data[region]["deceduti_ieri"]
  # regions_data[region]["delta_deceduti"] = (today - yesterday) / yesterday * 100
  regions_data[region]["delta_deceduti"] = (today - yesterday)

  regions_list.append(regions_data[region])

  # Manual reindex
  count = 0
  for index, row in regions_data[region].iterrows():
    regions_data[region].at[index, "day"] = count
    count += 1

  # X = 'totale_casi'
  X = 'day'

  axs[0, 0].plot(X, "totale_casi", label=region, data=regions_data[region], markersize=2, color=getColor(region), linewidth=2)
  # axs[0, 0].plot(X, "totale_attualmente_positivi", label=region, data=regions_data[region], marker='o', markersize=2, color=getColor(region), linewidth=0)
  axs[0, 1].plot(X, "delta_totale", label=region, data=regions_data[region], markersize=2, color=getColor(region), linewidth=2)

  axs[1, 0].plot(X, "terapia_intensiva", label=region, data=regions_data[region], markersize=2, color=getColor(region), linewidth=2)
  axs[1, 1].plot(X, "delta_terapia_intensiva", label=region, data=regions_data[region], markersize=2, color=getColor(region), linewidth=2)

  axs[2, 0].plot(X, "deceduti", label=region, data=regions_data[region], markersize=2, color=getColor(region), linewidth=2)
  axs[2, 1].plot(X, "delta_deceduti", label=region, data=regions_data[region], markersize=2, color=getColor(region), linewidth=2)


axs[0, 0].set_title('Totale casi')
axs[0, 1].set_title('Aumento casi su giorno precedente')

axs[1, 0].set_title('Terapia intensiva')
axs[1, 1].set_title('Aumento TI su giorno precedente')

axs[2, 0].set_title('Deceduti')
axs[2, 1].set_title('Aumento deceduti su giorno precedente')

axs[2, 1].legend(loc='upper center', bbox_to_anchor=(0, -0.2), ncol=5, fancybox=True, shadow=True)

fig.suptitle('Covid-19 [{}]\nNormalizzato su 100 casi a t0'.format(datetime.now().strftime("%d/%m/%Y")))
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=0.3)
plt.show()

# printRegions(FILTERED_REGIONS, regions_data)
