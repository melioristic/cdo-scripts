#!/bin/bash
 
#SBATCH --job-name=DLY_1981
#SBATCH --time=01:00:00
#SBATCH --mem-per-cpu=2G
#SBATCH --mail-type=ALL
 
#SBATCH --mail-user=itsmohitanand@gmail.com
 
# output files
#SBATCH -o dly_1981.out
#SBATCH -e dly_1981.err

module load foss/2019b CDO/1.9.8-Python-3.7.4

python script_1_daily_avg.py 1981