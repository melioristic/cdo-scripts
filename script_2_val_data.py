from netCDF4 import Dataset

file_dir = '/data/compoundx/bias-corrected-reanalysis/'
fname = 'Tair_WFDE5_CRU_dly_1979_v1.0.nc'
data  = Dataset(file_dir+fname)

print(data['time'])