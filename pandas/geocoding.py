import pandas
from geopy.geocoders import ArcGIS

df = pandas.read_csv("supermarkets.csv")
nom = ArcGIS()

df["Address"] = df["Address"]+", "+df["City"]+", "+df["State"]+", "+df["Country"]

df["Coordinates"] = df["Address"].apply(nom.geocode)

df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)

print(df.drop(df.columns[2:8],1))