import numpy as np
import scipy as misc
import pandas as pd

regions = ["Abruzzo", "Basilicata", "P.A. Bolzano", "Calabria", "Campania", "Emilia Romagna", "Friuli Venezia Giulia", "Lazio", "Liguria", "Lombardia", "Marche", "Molise", "Piemonte", "Puglia", "Sardegna", "Sicilia", "Toscana", "P.A. Trento", "Umbria", "Valle d'Aosta", "Veneto"]

# df = pd.read_csv('data.csv', sep=',' , header=None)
df = pd.read_csv('data.csv')
regions_data = {}

for region in regions:
  regions_data[region] = df[df["denominazione_regione"] == region]

print(regions_data)
