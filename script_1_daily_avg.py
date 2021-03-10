import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('year', help='computes daily average', type = str)
args = parser.parse_args()

year = args.year

list_out_file = [] 

file_directory = '/data/compoundx/bias-corrected-reanalysis/' 
out_year_file_name = 'Tair_WFDE5_CRU_dly_'+ year + '_v1.0.nc'

for month in range(1,13):
    
    month = str(month).zfill(2)
    
    input_file_name = 'Tair_WFDE5_CRU_'+ year + month + '_v1.0.nc'
    output_file_name = 'Tair_WFDE5_CRU_dly_'+ year + month + '_v1.0.nc'

    input_file_path = file_directory+input_file_name
    output_file_path = file_directory+output_file_name

    list_out_file.append(output_file_path)
    os.system('cdo daymean ' + input_file_path + ' ' +output_file_path)

infile = ''
for each in list_out_file:
    infile = infile + each + ' '

out_year_path = file_directory+ out_year_file_name

os.system('cdo cat ' + infile + out_year_path)

print(f'Calculated the daily mean for the {year}')