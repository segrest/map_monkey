#Used as a short hand to access often used Spatial References.
import arcpy
WGS84 =arcpy.SpatialReference(4326)
WebMerc=arcpy.SpatialReference(102100)
MSTM=arcpy.SpatialReference(102609)
NAD83=arcpy.SpatialReference(4269)
MSTM_HARN=arcpy.SpatialReference(102469)
MS_West=arcpy.SpatialReference(2255)
MS_East=arcpy.SpatialReference(2254)
esriDecimalDegrees=9102
esriFeet=9003
esriMeters=9001
esriKilometers=9036
esriMiles=9035
esriNauticalMiles=9030

def lookup(spatialRef):
    if spatialRef=='WGS84':
        return arcpy.SpatialReference(4326)
    elif spatialRef=='WebMerc':
        return arcpy.SpatialReference(102100)
    elif spatialRef=='MSTM':
        return arcpy.SpatialReference(102609)
    elif spatialRef=='NAD83':
        return arcpy.SpatialReference(4269)
    elif spatialRef=='MSTM_HARN':
        return arcpy.SpatialReference(102469)
    elif spatialRef=='MS_West':
        return arcpy.SpatialReference(2255)
    elif spatialRef=='WebMerc':
        return arcpy.SpatialReference(2254)
    else:
        return arcpy.SpatialReference(4326)
        
        
        
