import pandas as pd
from pyinaturalist import *
import inspect
from pyinaturalist_convert import *

# print(inspect.getfullargspec(get_observations))
observations = get_observations(q="Harmonia Axyridis", d1 = "01/01/2018", d2 = "30/11/2022", lat=53.94220, lng=-3.96803, radius=511, per_page=200)
# to_csv(observations, 'my_observations.csv')
dfList = []
nbPage =int(( observations["total_results"] / observations['per_page'] ) +1)
# print("nbpage :", nbPage )
# try:
    # tmp = get_observations(q="Harmonia Axyridis", d1 = "01/01/2018", d2 = "30/11/2022", lat=53.94220, lng=-3.96803, radius=511, per_page=400, page = 1)
# except Exception as e: 
    # print(e)
    
try:
    for page in range(1,nbPage+1):
        tmp = get_observations(q="Harmonia Axyridis", d1 = "01/01/2018", d2 = "30/11/2022", lat=53.94220, lng=-3.96803, radius=511, per_page=400, page = page)
        dfList.append(to_dataframe(tmp))
except Exception as e: 
    print(e)
    print("error came at page : ", page)
    df = pd.concat(dfList)
    df.to_csv("inat_data.csv", sep=",", index="False")
    print(len(df))


    
    

df = to_dataframe(observations)
