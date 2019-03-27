import glob
import driveanon
import pandas as pd

def arrTif(googID,stSlice,enSlice):
    # make a folder on your gdrive put your files in it and get the folder blob     id from the url.
    # make sure the folder permissions are set to public web under sharing ->       advanced settings

    files = driveanon.list_blobs(googID,
                             '.tif',
                            )


    # this will download all the files in that folder with a matching extension
    # to your local machine. best not to keep additional clutter in the folder,
    # as this library hasn't been extensively tested.

    # ensure that no extraneous tifs exist
    for f in files:
        driveanon.save(f,overwrite=True)
        
    pdArr = readTif(stSlice,enSlice)
    
    return pdArr

def readTif(stSlice,enSlice):

    # if rasters are named with date conventions, indicate the 
    # location of the date, arranged in YYYYMMDD format
    yrIdx = slice(stSlice,enSlice-4)
    moIdx = slice(stSlice+4,enSlice-2)
    dyIdx = slice(stSlice+6,enSlice)

    # create list of downloaded tif files
    pdArr = pd.DataFrame()
    pdArr['fname'] = glob.glob('*tif')
    pdArr['time'] = [pd.Timestamp(int(elem[yrIdx]),int(elem[moIdx]),                          int(elem[dyIdx])) for elem in pdArr['fname']]
    
    return pdArr

