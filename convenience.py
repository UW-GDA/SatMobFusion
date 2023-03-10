## Add reverse geocoding functions here

def bounding_box(points):
    x_coordinates, y_coordinates = zip(*points)
    return [(min(x_coordinates), min(y_coordinates)), (max(x_coordinates), max(y_coordinates))]

def get_rectangular_polygon_from_bounding_box(lon_min, lon_max, lat_min, lat_max):
    # return [(minx,maxy),(maxx,maxy),(maxx,miny),(minx,miny),(minx,maxy)]
    return [(lon_min,lat_max),(lon_max,lat_max),(lon_max,lat_min),(lon_min,lat_min),(lon_min,lat_max)]
