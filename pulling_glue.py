#!/usr/bin/env python3
import os
import sys
import random
import time
from random import seed, randint
import argparse
import platform
from datetime import datetime
import imp
from myPersonalFunctions import *
import glob
import numpy
# Useful codes
# os.system("awk '{print $NF}' all_wham.dat > e_total")
# tr " " "\n"
# sed 1d
# sort -u -k 3
# sed -e 's/+T//'
mypath = os.environ["PATH"]
os.environ["PATH"] = "/home/wl45/python/bin:/home/wl45/opt:" + mypath
my_env = os.environ.copy()

parser = argparse.ArgumentParser(description="This is my playground for current project")

# parser.add_argument("protein", help="the name of protein")
# parser.add_argument("template", help="the name of template file")
parser.add_argument("-t", "--test", help="test ", action="store_true", default=False)
parser.add_argument("--plot", action="store_true", default=False)
parser.add_argument("-d", "--debug", action="store_true", default=False)
parser.add_argument("--protein", default="2xov")
parser.add_argument("--dimension", type=int, default=1)
parser.add_argument("-f", "--freeEnergy", action="store_true", default=False)
parser.add_argument("--move", action="store_true", default=False)

args = parser.parse_args()


if(args.debug):
    do = print
    cd = print
else:
    do = os.system
    cd = os.chdir


if(args.freeEnergy):
    sim_list = "t250 t275 t300 t325 t350"
    temp_list = "250 275 300 325 350"
    do("mult_calc_cv.sc . '{}' 40 '{}' 100 200 10 30 400 0.12 0.9 2xov q".format(sim_list, temp_list))

if(args.plot):
    do("plotcontour.py pmf-200.dat -xmax 0.8 -xmin 0.2 -ymin 0.2 -ymax 0.8")

# ls */halfdata | sort -g | xargs cat > all_halfdata
# ls */tinydata | sort -g | xargs cat > all_tinydata
# awk '{print $3}' all_halfdata > p_total
# awk '{print $4}' all_halfdata > e_total
if(args.move):
    n = 40
    # temp_list = [250, 275, 300, 325, 350]
    temp_list = [200]
    cwd = os.getcwd()
    for temp in temp_list:
        for i in range(n):
            print(str(i))
            do("mkdir -p analysis/data/{}".format(i))
            do("cp simulation/{0}/{1}/halfdata analysis/data/{1}/".format(temp, i))
            cd("analysis/data/{}".format(i))
            do("tail -n 1000 halfdata > tinydata")
            cd(cwd)

if(args.test):
    # force_list = [1.0, 1.2, 1.4, 1.6, 1.8, 1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5]
    force_list = [round(i*0.1,2) for i in range(10)]
    # force_list = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    for force in force_list:
        do("mkdir {}".format(force))
        cd("{}".format(force))
        do("cp ../freeEnergy.slurm .")
        do("cp ../metadatafile .")
        do(
            "sed -i.bak 's/FORCE/" +
            str(force) +
            "/g' freeEnergy.slurm")
        do("sbatch freeEnergy.slurm")
        cd("..")
