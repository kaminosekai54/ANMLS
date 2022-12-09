import pandas as pd
from pyinaturalist import *
import inspect
from pyinaturalist_convert import *

# print(inspect.getfullargspec(get_observations))
# observations = get_observations(q="Harmonia Axyridis", d1 = "01/01/2018", d2 = "30/11/2022", lat=53.94220, lng=-3.96803, radius=511, per_page=200)
# to_csv(observations, 'my_observations.csv')
dfList = []
# nbPage =int(( observations["total_results"] / observations['per_page'] ) +1)
# print("nbpage :", nbPage )
# try:
    # tmp = get_observations(q="Harmonia Axyridis", d1 = "01/01/2018", d2 = "30/11/2022", lat=53.94220, lng=-3.96803, radius=511, per_page=400, page = 1)
# except Exception as e: 
    # print(e)
    
# try:
    # for page in range(1,nbPage+1):
        # tmp = get_observations(q="Harmonia Axyridis", d1 = "01/01/2018", d2 = "30/11/2022", lat=53.94220, lng=-3.96803, radius=511, per_page=400, page = page)
        # dfList.append(to_dataframe(tmp))
# except Exception as e: 
    # print(e)
    # print("error came at page : ", page)
    # df = pd.concat(dfList)
    # df = df[["quality_grade", "observed_on_details.date", "species_guess", "public_positional_accuracy", "taxon.name", "geojson.coordinates", "owners_identification_from_vision", "identification_count", "num_identification_disagreements", "location", "place_guess"]]
    # df.to_csv("inat_data.csv", sep=",", index="False")
    # print(len(df))


    
    


inat_df = pd.read_csv("inat_data.csv")
inat_df = inat_df [["quality_grade", "observed_on_details.date", "species_guess", "public_positional_accuracy", "taxon.name", "geojson.coordinates", "owners_identification_from_vision", "identifications_count", "num_identification_disagreements", "location", "place_guess"]]
# print(inat_df)
# coordDf = pd.DataFrame(inat_df.location.tolist(), columns=["latitude", "longitude"])
latitude = []
for val in inat_df.location.tolist():
    latitude.append(val[0])
    
longitude= []
for val in inat_df.location.tolist():
    longitude.append(val[1])
  
inat_df= inat_df.assign(latitude = latitude)
inat_df= inat_df.assign(longitude = longitude)

article_df = pd.read_csv("article_data.csv")
article_df.columns= article_df.columns.str.lower()

article_df.to_csv("article_data.csv", sep=",", index=False)
inat_df.to_csv("inat_data_filtered.csv", sep=",", index=False)

