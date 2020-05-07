# Load the Pandas libraries with alias 'pd'
import pandas as pd
import json



def df_to_geojson(df,id,name,region, lat='latitude', lon='longitude'):
    geojson = {'type':'FeatureCollection', 'features':[]}
    for _, row in df.iterrows():
        feature = {'type':'Feature',
                   'properties':{},
                   'geometry':{'type':'Point',
                               'coordinates':[]}}
        feature['geometry']['coordinates'] = [row[lon],row[lat]]
        feature['properties'][id] = row[id]
        feature['properties'][name] = row[name]
        feature['properties'][region] = row[region]

        geojson['features'].append(feature)
    return geojson



# Read data from file 'filename.csv'
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later)
df_data = pd.read_csv("actions_coordinates.csv",delimiter=';')
# Preview the first 5 lines of the loaded data
df_data.head()
print(df_data)


geojson_str = df_to_geojson(df_data,'id','Наименование','Регион',lat='Широта', lon='Долгота')

print(geojson_str)
import sys
import pandas as pd
import json
#import datetime

#
#
# # CSV to DataFrame
# dataframe = pd.read_csv(csv_filename, delimiter=';', parse_dates=['DeviceTime'], infer_datetime_format=True, na_values=[''])
#
# #
# #print(dataframe)
#
# dataframe.dtypes
#
#
# json_result_string = dataframe.to_json(
#     orient='records',
#     double_precision=12,
#     date_format='iso'
# )
#
# #Generate GeoJson
#
# json_result = json.loads(json_result_string)
#
# geojson = {
#     'type': 'FeatureCollection',
#     'features': []
# }
# for record in json_result:
#     geojson['features'].append({
#         'type': 'Feature',
#         'geometry': {
#             'type': 'Point',
#             'coordinates': [record['Longitude'], record['Latitude']],
#         },
#         'properties': record,
#     })
#
#
# Generate geojson filename
geojson_filename = "crm.geojson"
#
#
# #Record geojson file
with open(geojson_filename, 'w') as f:
     f.write(json.dumps(geojson_str, indent=2))
#
#
# #Print geojson file
# print ("See file:  "+ geojson_filename)
#
