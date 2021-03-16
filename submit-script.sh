#!/bin/bash
#SBATCH --job-name=DLY_Rainf
#SBATCH --time=02:00:00
#SBATCH --mem-per-cpu=4G
#SBATCH --mail-type=ALL
#SBATCH --mail-user=itsmohitanand@gmail.com
# output files
#SBATCH -o dly_%a.out
#SBATCH -e dly_%a.err

#SBATCH --array=1979-2018

module load foss/2019b CDO/1.9.8-Python-3.7.4

python script_1_daily_avg.py $SLURM_ARRAY_TASK_ID