import os

list_out_file = [] 

file_directory = '/data/compoundx/bias-corrected-reanalysis/Rainf/' 

out_fname = file_directory + 'Rainf_WFDE5_CRU_dly_v1.0.nc'

list_str = ''
for year in range(1979, 2019):
    out_year_file_name = file_directory + 'Rainf_WFDE5_CRU_dly_'+ str(year) + '_v1.0.nc'

    list_str = list_str+out_year_file_name+' '

print(list_str)

os.system('cdo cat ' + list_str + out_fname)

