import pandas as pd
import geopandas as gpd
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def textplot(
    keywords,
    title='Cases in {year}',
    years=[2016],
    casesfile='../csv/cases/cases/small_cases_{year}.csv',
    codesfile='../cleaned_csv/cases_district_key.csv',
    shapefile='../shapefiles/in_district.shp',
    typesfile='../csv/keys/keys/type_name_key.csv',
):
    # read the codes csv file
    codes = pd.read_csv(codesfile)

    # keep only the columns we need
    codes = codes[['state_code', 'dist_code', 'pc11_district_id']]

    # read the shapefile
    shapes = gpd.read_file(shapefile)

    # convert dtcode11 to int
    shapes['dtcode11'] = shapes['dtcode11'].astype(int, errors='ignore')

    # read the types csv file
    types = pd.read_csv(typesfile)
    # drop unnecessary columns
    types.drop(columns=['year', 'count'], inplace=True)

    regex = '|'.join(keywords)

    # years = range(2010, 2018 + 1)
    # years = [2016]

    for year in years:

        df = pd.read_csv(casesfile.format(year=year))

        # drop unnecessary columns
        df = df[['year', 'state_code', 'dist_code', 'type_name']]

        # add a column for criminal cases

        # merge the dataframes
        df = df.merge(types, on='type_name')
        df['criminal'] = df['type_name_s'].str.lower().str.contains(regex)

        df.drop(columns=['type_name_s', 'type_name'], inplace=True)

        # group and count
        df = df.groupby(['year', 'state_code', 'dist_code',
                         'criminal']).size().reset_index(name='count')

        # filter only criminal cases
        df = df[df['criminal'] == True].drop(columns=['criminal'])

        # merge with codes
        df = df.merge(codes, on=['state_code', 'dist_code'
                                 ]).drop(columns=['state_code', 'dist_code'])

        # rename the column to dtcode11
        df.rename(columns={'pc11_district_id': 'dtcode11'}, inplace=True)

        # convert dtcode11 to int
        df['dtcode11'] = df['dtcode11'].astype(int, errors='ignore')

        # print(df.head())

        # merge with shapes
        map = shapes.merge(df, on='dtcode11', how='left')
        # print(map.head())

        minima = df['count'].min()
        maxima = df['count'].max()
        norm = matplotlib.colors.Normalize(vmin=minima, vmax=maxima, clip=True)
        mapper = cm.ScalarMappable(norm=norm, cmap=cm.Reds)

        # plot the map
        plot = map.plot(
            # random colors
            # color=map['dtcode11'].map(lambda x: 'C' + str(x)),
            color=map['count'].map(lambda x: mapper.to_rgba(x)),
            # column='count',
            edgecolor='black',
            linewidth=0.1,
        )
        plot.set_axis_off()
        plot.set_title(title.format(year=year))
        plt.show()

        # # save to csv
        # df.to_csv(f'../data/cases/crimes_{year}.csv', index=False)
