import geopandas as gpd
import pandas as pd
import skmob

def preprocess_mobile_data(df, state_df, crs='EPSG:4269', max_speed_kmh=400, spatial_radius_km=0.2):
    gdf = gpd.GeoDataFrame(df, crs=crs, geometry=gpd.points_from_xy(df['lon'], df['lat']))

    # Exclude points outside of relevant state
    gdf = gpd.sjoin(gdf, state_df, how='left', predicate='within')

    # Create datetime column using timestamps
    gdf['datetime'] = pd.to_datetime(gdf['timestamp'], unit='s')

    # Keep first 13 columns
    #comp1_gpd = comp1_gpd.iloc[:, :13]
    # Create a date column
    #comp1_gpd['date'] = comp1_gpd['datetime'].dt.date
    tdf = skmob.TrajDataFrame(gdf, latitude='lat', longitude='lon', datetime='datetime', user_id='uid')
    print('Original number of points: ', tdf.shape[0])
    f_tdf = skmob.preprocessing.filtering.filter(tdf, max_speed_kmh=max_speed_kmh, include_loops=False)
    print('Number of points after filtering: ', f_tdf.shape[0])
    fc_tdf = skmob.preprocessing.compression.compress(f_tdf, spatial_radius_km=spatial_radius_km)
    print('Number of points after compression: ', fc_tdf.shape[0])

    preproc_gdf = gpd.GeoDataFrame(fc_tdf, crs=crs, geometry=gpd.points_from_xy(fc_tdf['lng'], fc_tdf['lat']))
    preproc_gdf['datetime'] = pd.to_datetime(preproc_gdf['datetime'], format='%Y-%m-%d %H:%M:%S')  
    return preproc_gdf  

def bounding_box(points):
    x_coordinates, y_coordinates = zip(*points)
    return [(min(x_coordinates), min(y_coordinates)), (max(x_coordinates), max(y_coordinates))]

def get_rectangular_polygon_from_bounding_box(lon_min, lon_max, lat_min, lat_max):
    # return [(minx,maxy),(maxx,maxy),(maxx,miny),(minx,miny),(minx,maxy)]
    return [(lon_min,lat_max),(lon_max,lat_max),(lon_max,lat_min),(lon_min,lat_min),(lon_min,lat_max)]
