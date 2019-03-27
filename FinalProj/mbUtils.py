import rasterio
from rasterio.mask import mask
import numpy as np
import pandas as pd

def clip(gf,dem1,dem2,outline):
    gf.z1 = mask(dem1,[outline[1]],crop=True)
    gf.z2 = mask(dem2,[outline[1]],crop=True)
    
    gf.z1[0][gf.z1[0] < 0.0] = np.nan
    gf.z2[0][gf.z2[0] < 0.0] = np.nan
    
def surfdz(gf,time1,time2):
    gf.dz = gf.z2[0][0] - gf.z1[0][0]
    gf.dzdt = np.divide(gf.dz,(time2-time1).days)
    
def get_stats(group):
    return {'min': group.min(),'max': group.max(),'count': group.count(),'mean': group.mean()}
    
def binbyElev(EL,DIF,bins):
    elevs = np.ravel(EL)
    diffs = np.ravel(DIF)
    
    df = pd.DataFrame({'elevations': elevs,'diffs': diffs,})
    df['elevation_contours'] = pd.cut(df['elevations'],bins)
    
    mb =df['diffs'].groupby(df['elevation_contours']).apply(get_stats).unstack()
    
    return mb
