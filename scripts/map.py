import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import pandas as pd
import seaborn as sns
import json
from fuzzywuzzy import fuzz, process

# codes = json.load(open('json/district_codes.json'))

# # read the csv file
# codes = pd.read_csv('cleaned_csv/cases_district_key.csv')

# judges = pd.read_csv('cleaned_csv/judges_clean.csv')

# print(shapes.describe())
# print(codes.describe())

# only keep the columns we need
# codes = codes[['state_code', 'dist_code', 'district_name']]

# merge the dataframes

# # to fuzzy merge
# shapes['pc11_district_id'] = shapes.pc11_district_id.apply(
#     lambda x: '*' + [process.extract(x, codes.district_name, limit=1)][0][0][0]
#     if x == '' else x)

# names = shapes[['dtcode11', 'dtname', 'pc11_district_id']].to_dict('records')

# json.dump(names, open('json/district_names.json', 'w'))

# shapes.merge(codes, left_on='key', right_on='district_name')

# shapes.merge(codes, left_on='dtcode11', right_on='pc11_district_id')

# test unmatched names - found many errors
# names = shapes[['key', 'dtname'
#                 ]][shapes['key'] != shapes['dtname']].to_dict('records')

# json.dump(names, open('json/district_names.json', 'w'))


def plot_district_map(shapefile='shapefiles/in_district.shp',
                      data=None,
                      names=False,
                      title='Districts of India'):
    # read the shapefile
    shapes = gpd.read_file(shapefile)

    # plot the map
    plot = shapes.plot(
        color=data if data else shapes['dtcode11'].map(lambda x: 'C' + str(x)),
        edgecolor='black',
        linewidth=0.1)
    plot.set_axis_off()
    plot.set_title(title)

    if names:
        # annotate district names
        shapes.apply(lambda x: plot.annotate(
            text=x['dtcode11'],
            fontsize=5,
            xy=x.geometry.centroid.coords[0],
            ha='center',
        ),
                     axis=1)

    plt.show()
