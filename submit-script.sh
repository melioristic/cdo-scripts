#!/bin/bash
 
#SBATCH --job-name=DLY_1982
#SBATCH --time=02:00:00
#SBATCH --mem-per-cpu=4G
#SBATCH --mail-type=ALL
 
#SBATCH --mail-user=itsmohitanand@gmail.com
 
# output files
#SBATCH -o dly_1982.out
#SBATCH -e dly_1982.err

module load foss/2019b CDO/1.9.8-Python-3.7.4

python script_1_daily_avg.py 1982