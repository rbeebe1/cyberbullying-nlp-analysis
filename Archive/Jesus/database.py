# Dependencies
import pandas as pd
import os

# Import json files into MongoDB
os.system("mongoimport --type json -d project4 -c youtube --drop --jsonArray ../vinny/final_data.json")