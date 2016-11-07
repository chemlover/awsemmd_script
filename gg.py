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
parser.add_argument("-f", "--freeEnergy", help="free energy data sort ", action="store_true", default=False)
parser.add_argument("--fix", help="fix ", action="store_true", default=False)
parser.add_argument("--wham", help="wham analysis ", action="store_true", default=False)
parser.add_argument("--wham400", help="wham analysis in temp 400 ", action="store_true", default=False)
parser.add_argument("-p", "--plot", help="plot", action="store_true", default=False)
args = parser.parse_args()

def calQo():
    os.system("python2 ~/opt/script/CalcQValue_multi.py 2lhc dump.lammpstrj qo 1")


# def wham_analysis():
#     os.system("mkdir -p wham")
#     os.system("rm wham/all.dat")
#     os.system("rm wham/*_total")
#     os.chdir("300")
#     for i in range(20):
#         # os.system("cat {}/halfdata.dat >> ../wham/all.dat".format(i))
#         # os.system("tail -n+3 rerun_"+str(i)+"/wham.dat | awk '{print $3}' | tail -n 5000 >> ../wham/p_total")
#         os.system("tail -n+2 " + str(i) + "/wham.dat | awk '{print $3}' | tail -n 5000 >> ../wham/p_total")
#         os.system("tail -n+2 " + str(i) + "/wham.dat | awk '{print $5}' | tail -n 5000 >> ../wham/e_total")
#         os.system("tail -n+2 " + str(i) + "/wham.dat | awk '{print $2}' | tail -n 5000 >> ../wham/qw_total")
#
#         os.chdir(str(i))
#         os.system("cp ~/opt/gagb/2lhc_part.pdb .")
#         os.system("awk '{if ((!((($1>0 && $1<25) || ($1>159 && $1<200) ) && $3>-10)  ) ) print }' dump.lammpstrj > data_test")
#         os.system("python2 ~/opt/script/CalcQValue.py 2lhc_part.pdb data_test test")
#         os.system("tail -n +2 test > qw_ga.dat")
#         os.chdir("..")
#         os.system("tail -n 5000 " + str(i) + "/qw_ga.dat >> ../wham/qw_ga_total")
#         # os.system("tail -n+3 rerun_{}/wham.dat | awk '{print $3}' >> ../wham/qo_total".format(str(i)))
#     os.chdir("../wham")
#     # os.system("awk '{print $2}' all.dat > Qw_total")
#     # os.system("awk '{print $3}' all.dat > Qgb_total")
#     # os.system("awk '{print $1}' all.dat > qwa_total")
#     # os.system("awk '{print $4}' all.dat > e_total")
#     # os.system("awk '{print $6}' all.dat > p_total")
#     os.system("cp ~/opt/wham_analysis/*.m .")
#     os.chdir("..")
#     os.system("~/opt/script/wham/fused_calc_cv.sc wham/ 2lhd 20 300 250 350 10 50 200 0.05 1")
# protein_name = args.template.split('_', 1)[-1].strip('/')
# protein_name = args.protein.strip('/')
    # name = "ga_2m"
# exec(open("config.py").read())
# n = number_of_run
# steps = simulation_steps
# # protein_name = protein_name
#
# import experiment_analysis
# os.system("cp ~/opt/gagb/energy2.gp .")
# os.system("gnuplot energy2.gp ")
# os.system("open energy2.pdf ")

def wham_analysis():
    os.system("mkdir -p wham")
    os.system("rm wham/all.dat")
    os.system("rm wham/*_total")
    os.chdir("300")
    for i in range(20):
        # os.system("cat {}/halfdata.dat >> ../wham/all.dat".format(i))
        # os.system("tail -n+3 rerun_"+str(i)+"/wham.dat | awk '{print $3}' | tail -n 5000 >> ../wham/p_total")
        os.system("tail -n+2 " + str(i) + "/wham.dat | awk '{print $4}' | tail -n 2000 >> ../wham/p_total")
        os.system("tail -n+2 " + str(i) + "/wham.dat | awk '{print $6}' | tail -n 2000 >> ../wham/e_total")
        os.system("tail -n+2 " + str(i) + "/wham.dat | awk '{print $2}' | tail -n 2000 >> ../wham/qw_total")

        os.chdir(str(i))
        os.system("cp ~/opt/gagb/2lhc_part.pdb .")
        os.system("awk '{if ((!((($1>0 && $1<25) || ($1>159 && $1<200) ) && $3>-10)  ) ) print }' dump.lammpstrj > data_test")
        os.system("python2 ~/opt/script/CalcQValue.py 2lhc_part.pdb data_test test")
        os.system("tail -n +2 test > qw_ga.dat")
        os.chdir("..")
        os.system("tail -n 2000 " + str(i) + "/qw_ga.dat >> ../wham/qw_ga_total")
        # os.system("tail -n+3 rerun_{}/wham.dat | awk '{print $3}' >> ../wham/qo_total".format(str(i)))
    os.chdir("../wham")
    # os.system("awk '{print $2}' all.dat > Qw_total")
    # os.system("awk '{print $3}' all.dat > Qgb_total")
    # os.system("awk '{print $1}' all.dat > qwa_total")
    # os.system("awk '{print $4}' all.dat > e_total")
    # os.system("awk '{print $6}' all.dat > p_total")
    os.system("cp ~/opt/wham_analysis/*.m .")
    os.chdir("..")
    os.system("~/opt/script/wham/fused_calc_cv.sc wham/ 2lhd 20 300 250 350 10 50 200 0.05 1")


def wham_analysis400():
    os.system("mkdir -p wham400")
    os.system("rm wham400/all.dat")
    os.system("rm wham400/*_total")
    os.chdir("400")
    for i in range(18):
        os.system("cat {}/halfdata.dat >> ../wham400/all.dat".format(i))
        os.system("tail -n+3 rerun_"+str(i)+"/wham.dat | awk '{print $3}' | tail -n 5000 >> ../wham400/p_total")

    os.chdir("../wham400")
    os.system("awk '{print $2}' all.dat > Qw_total")
    os.system("awk '{print $3}' all.dat > Qgb_total")
    os.system("awk '{print $1}' all.dat > qwa_total")
    os.system("awk '{print $4}' all.dat > e_total")
    os.system("cp ~/opt/wham_analysis/*.m .")
    os.chdir("..")
    os.system("~/opt/script/wham/fused_calc_cv.sc wham400/ 2lhd 18 400 350 450 10 50 200 0.05 0.9")


def free_energy_analysis():
    temp_list = [300, 400]
    n = 20
    for temp in temp_list:
        os.chdir(str(temp))
        for i in range(n):
            os.chdir(str(i))
            # os.system("awk '{print $2}' wham.dat | tail -n +2 > p.dat")
            # os.system("awk '{print $3}' wham.dat | tail -n +2 > p2.dat")
            # os.system("cp ~/opt/gagb/2lhc_part.pdb .")
            # os.system("awk '{if ((!((($1>0 && $1<25) || ($1>159 && $1<200) ) && $3>-10)  ) ) print }' dump.lammpstrj > data_test")
            # os.system("python2 ~/opt/script/CalcQValue.py 2lhc_part.pdb data_test test")
            # os.system("tail -n +2 test > q_ga_part.dat")
            # os.system("python2 ~/opt/script/CalcQValue.py 2lhc dump.lammpstrj q_ga_included.dat")
            # os.system("tail -n +2 q_ga_included.dat > q_ga.dat")
            # os.system("python2 ~/opt/script/CalcQValue.py 2lhd dump.lammpstrj q_gb_included.dat")
            # os.system("tail -n +2 q_gb_included.dat > q_gb.dat")
            os.system("cp ~/opt/gagb/nativecoords_g* .")
            os.system("mv nativecoords_ga.dat nativecoords.dat")
            os.system("python2 ~/opt/script/CalcQValue_multi.py 2lhc dump.lammpstrj qo 1")
            os.system("tail -n +2 qo > qo.dat")
            os.system("paste q_ga.dat q_ga_part.dat q_gb.dat p.dat p2.dat qo.dat > data.dat")
            os.system("tail -n 5000 data.dat > halfdata.dat")
            os.chdir("..")
        os.chdir("..")


def plot():
    print("Plotting")
    # os.system("python2 ~/opt/script/CalcQValue.py 2lhc dump2.lammpstrj qw.dat")
    os.system("cp ~/opt/temp.gp .")
    out_file = "test.pdf"
    out = "'out_file_name=\"{}\"'".format(out_file)
    in_file = "gb_sequence/wham.dat_2"
    gp_in = "'in_file_name=\"{}\"'".format(in_file)
    in_file_2 = "0/wham.dat"
    gp_in_2 = "'in_file_name_2=\"{}\"'".format(in_file_2)
    os.system("gnuplot -e {} -e {} -e {} temp.gp ".format(gp_in, gp_in_2, out))
    os.system("open test.pdf ")


def fix():
    n = 20
    os.chdir("analysis")
    os.system("rm highest_q_gb")
    os.system("rm highest_q")
    for i in range(n):
        os.chdir(str(i))
        # os.system("tail -n 5000 wham.dat > halfdata.dat")
        os.system("cp ~/opt/gagb/2lhc.pdb .")
        os.system("cp ~/opt/gagb/2lhd.pdb .")
        os.system("python2 ~/opt/script/CalcQValue.py 2lhc.pdb dump.lammpstrj ga")
        os.system("tail -n 1000 ga | sort | tail -n 1 > ga_highest")
        os.system("cat ga_highest >> ../highest_q")

        os.system("python2 ~/opt/script/CalcQValue.py 2lhd dump.lammpstrj gb")
        os.system("tail -n 1000 gb | sort | tail -n 1 > gb_highest")
        os.system("cat gb_highest >> ../highest_q_gb")
        os.chdir("..")


def rerun():
    n = 20
    for i in range(n):
        os.system("cp -r {0} rerun_{0}".format(str(i)))
        os.chdir("rerun_"+str(i))
        os.system("cp ~/opt/gagb/rerun.slurm .")
        os.system("cp ~/opt/gagb/2lhc_rerun.in .")
        os.system("sbatch rerun.slurm")
        os.chdir("..")


def rerun_wham_analysis():
    os.system("mkdir -p wham")
    os.system("rm wham/all.dat")
    os.system("rm wham/*_total")
    os.chdir("300")
    for i in range(20):
        # os.system("cat {}/halfdata.dat >> ../wham/all.dat".format(i))
        # os.system("tail -n+3 rerun_"+str(i)+"/wham.dat | awk '{print $3}' | tail -n 5000 >> ../wham/p_total")
        os.system("tail -n+2 rerun_" + str(i) + "/wham.dat | awk '{print $3}' | tail -n 2000 >> ../wham/p_total")
        os.system("tail -n+2 rerun_" + str(i) + "/wham.dat | awk '{print $6}' | tail -n 2000 >> ../wham/e_total")
        os.system("tail -n+2 rerun_" + str(i) + "/wham.dat | awk '{print $2}' | tail -n 2000 >> ../wham/qw_total")

        # os.chdir(str(i))
        # os.system("cp ~/opt/gagb/2lhc_part.pdb .")
        # os.system("awk '{if ((!((($1>0 && $1<25) || ($1>159 && $1<200) ) && $3>-10)  ) ) print }' dump.lammpstrj > data_test")
        # os.system("python2 ~/opt/script/CalcQValue.py 2lhc_part.pdb data_test test")
        # os.system("tail -n +2 test > qw_ga.dat")
        # os.chdir("..")
        os.system("tail -n 2000 " + str(i) + "/qw_ga.dat >> ../wham/qw_ga_total")
        # os.system("tail -n+3 rerun_{}/wham.dat | awk '{print $3}' >> ../wham/qo_total".format(str(i)))
    os.chdir("../wham")
    # os.system("awk '{print $2}' all.dat > Qw_total")
    # os.system("awk '{print $3}' all.dat > Qgb_total")
    # os.system("awk '{print $1}' all.dat > qwa_total")
    # os.system("awk '{print $4}' all.dat > e_total")
    # os.system("awk '{print $6}' all.dat > p_total")
    os.system("cp ~/opt/wham_analysis/*.m .")
    os.chdir("..")
    os.system("~/opt/script/wham/fused_calc_cv.sc wham/ 2lhd 20 300 250 350 10 50 200 0.05 1")
#rerun()
# rerun_wham_analysis()


#rerun()

if(args.wham):
    wham_analysis()
if(args.wham400):
    wham_analysis400()
if(args.freeEnergy):
    free_energy_analysis()
if(args.fix):
    fix()
if(args.plot):
    plot()
## -------------Pulling--------
# os.system("cp ~/opt/small_script/springForce.plt .")
# os.system("cp ~/opt/small_script/springForce_smooth.plt .")
# os.system("gnuplot springForce.plt")
# os.system("gnuplot springForce_smooth.plt")
# os.system("open springForce.pdf")
# os.system("open springForce_smooth.pdf")
# SpringConstant_list = [0.0001, 0.00001, 0.000001, 0.0000001]
# for SpringConstant in SpringConstant_list:
#     name = "spring"+str(SpringConstant)
#     os.system("mkdir "+name)
#     os.chdir(name)
#     os.system("cp -r ../2xov/ .")
#     os.system("cp ../variables.dat .")
#     os.chdir("2xov")
#     os.system(  # replace SIMULATION_STEPS with specific steps
#         "sed -i.bak 's/SpringForce/'" +
#         str(SpringConstant) +
#         "'/g' "+protein_name+".in")
#     os.chdir("..")
#     os.system("run.py 2xov/ -s 2")
#     os.chdir("..")
# # -----------------GAGB------------------------------
# # number_of_run_list = [2,  4, 8, 16]
# number_of_run_list = [5, 8, 32]
# for n in number_of_run_list:
#     name = "ga_"+str(n)+"m"
#     # os.system("mkdir "+name)
#     os.system("cp -r 2lhd.pdb "+name)
#
#     # os.system("cp -r 2lhc variables.dat "+name)
#     os.chdir(name)
#     for i in range(20):
#         os.chdir("analysis/"+str(i))
#         os.system("cp ../../2lhd.pdb .")
#         os.system("python2 ~/opt/script/CalcQValue.py 2lhd.pdb dump.lammpstrj q_gb.dat")
#         os.system("python2 ~/opt/script/CalcQValue.py 2lhc.pdb dump.lammpstrj q_ga.dat")
#         os.system("cp ~/opt/small_script/qw_gagb.plt .")
#         os.system("gnuplot qw_gagb.plt")
#         os.system("mv qw_gagb.pdf ../../results/qw_gagb_{0}.pdf".format(str(i)))
#         os.chdir("../..")
#     os.chdir("..")
#
# for n in number_of_run_list:
#     name = "ga_"+str(n)+"m"
#     # os.system("mkdir "+name)
#     os.system("cp -r 2lhd.pdb "+name)
#
#     # os.system("cp -r 2lhc variables.dat "+name)
#     os.chdir(name)
#     for i in range(20):
#         os.chdir("analysis/"+str(i))
#         os.system("paste q_ga.dat q_gb.dat > q_gagb.dat")
#         os.system("cp ~/opt/small_script/qw_ga-gb.plt .")
#         os.system("gnuplot qw_ga-gb.plt")
#         os.system("mv qw_ga-gb.pdf ../../results/qw_ga-gb_{0}.pdf".format(str(i)))
#         os.chdir("../..")
#     os.system("cp ~/opt/small_script/qw_ga_all.plt .")
#     os.system("gnuplot qw_ga_all.plt")
#     os.system("cp ~/opt/small_script/qw_gb_all.plt .")
#     os.system("gnuplot qw_gb_all.plt")
#     os.system("cp ~/opt/small_script/qw_diff_all.plt .")
#     os.system("gnuplot qw_diff_all.plt")
#     os.chdir("..")
# # -----------------GAGB------------------------------

# # -----------------GAGB------------------------------
# # number_of_run_list = [2,  4, 8, 16]
# # number_of_run_list = [5, 8, 32]
# number_of_run_list = [32]
# for n in number_of_run_list:
#     name = "gb_"+str(n)+"m"
#     # os.system("mkdir "+name)
#     os.system("cp -r 2lhc.pdb "+name)
#     os.system("cp -r 2lhd.pdb "+name)
#     # os.system("cp -r 2lhc variables.dat "+name)
#     os.chdir(name)
#     for i in range(20):
#         os.chdir("analysis/"+str(i))
#         os.system("cp ../../2lhc.pdb .")
#         os.system("cp ../../2lhd.pdb .")
#         os.system("python2 ~/opt/script/CalcQValue.py 2lhd.pdb dump.lammpstrj q_gb.dat")
#         os.system("python2 ~/opt/script/CalcQValue.py 2lhc.pdb dump.lammpstrj q_ga.dat")
#         os.system("cp ~/opt/small_script/qw_gagb.plt .")
#         os.system("gnuplot qw_gagb.plt")
#         os.system("mv qw_gagb.pdf ../../results/qw_gagb_{0}.pdf".format(str(i)))
#         os.chdir("../..")
#     os.chdir("..")
#
# for n in number_of_run_list:
#     name = "gb_"+str(n)+"m"
#     # os.system("mkdir "+name)
#     os.system("cp -r 2lhd.pdb "+name)
#
#     # os.system("cp -r 2lhc variables.dat "+name)
#     os.chdir(name)
#     for i in range(20):
#         os.chdir("analysis/"+str(i))
#         os.system("paste q_ga.dat q_gb.dat > q_gagb.dat")
#         os.system("cp ~/opt/small_script/qw_ga-gb.plt .")
#         os.system("gnuplot qw_ga-gb.plt")
#         os.system("mv qw_ga-gb.pdf ../../results/qw_ga-gb_{0}.pdf".format(str(i)))
#         os.chdir("../..")
#     os.system("cp ~/opt/small_script/qw_ga_all.plt .")
#     os.system("gnuplot qw_ga_all.plt")
#     os.system("cp ~/opt/small_script/qw_gb_all.plt .")
#     os.system("gnuplot qw_gb_all.plt")
#     os.system("cp ~/opt/small_script/qw_diff_all.plt .")
#     os.system("gnuplot qw_diff_all.plt")
#     os.chdir("..")
# # -----------------GAGB------------------------------


# simulation_steps = 4 * 10**6
# warm_up_steps = 10 * 10**5
#
# seed(datetime.now())
# n= 20
# vmd = "/Applications/VMD\ 1.9.2.app/Contents/MacOS/startup.command"
#
# os.system("BuildAllAtomsFromLammps.py dump.lammpstrj movie")
# os.system("cp ~/opt/plot_scripts/2xov_movie.tcl .")
# os.system(vmd+" -e 2xov_movie.tcl ")
# os.system("mkdir -p MyResults")
# for i in range(n):
#     print(i)
#     os.chdir("analysis/"+str(i))
#     os.system("cp ~/opt/plot_scripts/2xov_movie_screenshot.tcl .")
#     os.system(vmd+" -e 2xov_movie_screenshot.tcl")
#     os.system("cp frame1000.tga ../../MyResults/frame"+str(i)+"_1000.tga")
#     #os.system("cp frame450.tga ../Results/frame"+folder_name+"_450.tga")
#     # os.system("movie.py "+protein_name)
#     os.chdir("../..")
#     # analysis

# folder_name = ""
# result_folder = "WeiLu_Aug_07"

# protein_list = ['T089', 'T120', 'T251', 'TOP7', '1UBQ']
# sublist = ['']
# # sublist = ['_ha', '_he']
# # sublist = ['_lp', '_he_lp']
# # folder_list = []
# for protein in protein_list:
#     for sub in sublist:
#         folder_name = protein+sub
#         os.chdir(folder_name)
#         os.chdir("best_2nd")
#         os.system("pymol ~/opt/plot_scripts/align.pml > matrix.dat")
#         os.system("head -n 70 matrix.dat | tail -n 20 > cealign_matrix.dat")
#         # for i in range(19, -1, -1):
#         #     os.system("mv {}.pdb {}.pdb".format(i, i+1))
#         os.chdir("../..")
# os.chdir(protein)
# os.chdir("best_1st")
# os.system("python3 ~/opt/small_script/cross_q.py")
# os.chdir("..")
# os.chdir("best_2nd")
# os.system("python3 ~/opt/small_script/cross_q.py")
# os.chdir("..")
# os.chdir("..")
# n = 3
# for i in range(n):
#     # simulation set up
#     folder_name = str(i)
#     os.system("mkdir -p "+folder_name)
#     os.system("cp -r "+args.protein+"* "+folder_name)
#     os.chdir(folder_name)
#     os.system("cp ../../helix_less/simulation/"+str(i)+"/restart.4000000 .")
#     os.system(  # replace SIMULATION_STEPS with specific steps
#         "sed -i.bak 's/WARM_UP_STEPS/'" +
#         str(warm_up_steps) +
#         "'/g' "+protein_name+".in")
#     os.system(  # replace RANDOM with a radnom number
#             "sed -i.bak 's/RANDOM/'" +
#             str(randint(1, 10**6)) +
#             "'/g' "+protein_name+".in")
#     os.system(  # replace SIMULATION_STEPS with specific steps
#             "sed -i.bak 's/SIMULATION_STEPS/'" +
#             str(simulation_steps) +
#             "'/g' "+protein_name+".in")
# # if(platform.system() == 'Darwin'):
# #     os.system("/Users/weilu/Documents/lammps-9Oct12_modified/src/lmp_serial \
# #     < "+protein_name+".in")
#     if(platform.system() == 'Darwin'):
#         os.system("/Users/weilu/Documents/lammps-9Oct12_modified/src/lmp_serial \
#         < "+protein_name+".in")
#     elif(platform.system() == 'Linux'):
#         os.system("cp ~/opt/run.slurm .")
#         os.system(  # replace PROTEIN with pdb name
#                 "sed -i.bak 's/PROTEIN/'" +
#                 protein_name +
#                 "'/g' run.slurm")
#         os.system("sbatch run.slurm")
#     else:
#         print("system unkown")
#     os.chdir("..")
# exit(1)

# w_helix_list = [0.1, 0.5, 1, 1.5]
# m_helix_list = [0.1, 0.5, 1, 1.5]
#
# for i in range(len(w_helix_list)):
#     w = w_helix_list[i]
#     for j in range(len(m_helix_list)):
#
#         # m = m_helix_list[j]
#         folder_name = str(i)+"_"+str(j)
#         # os.system("cd "folder_name)
#         os.chdir(folder_name)
#         # os.system("analysis.py 2xov/")
#         # os.system("echo "+folder_name+" >> ../all")
#         os.system("sort -k 3 analysis/list_of_max_q > ../data/"+folder_name)
#         os.chdir("..")
#         # os.system("mkdir "+folder_name)
#         # os.chdir(folder_name)
#         # os.system("cp -r ../2xov .")
#         # os.chdir("2xov")
#         # os.system(
#         #         "sed -i.bak 's/W_HELIX/'" +
#         #         str(w) +
#         #         "'/g' fix_backbone_coeff.data")
#         # os.system(
#         #         "sed -i.bak 's/M_HELIX/'" +
#         #         str(m) +
#         #         "'/g' fix_backbone_coeff.data")
#         # os.chdir("..")
#         # os.system("run.py 2xov/ -n 5")

# os.system("cp ~/opt/gg.py this_gg.py")
# for i in range(5):
#     os.system("mkdir "+str(i))
#     os.chdir(str(i))
#     os.system("cp -r ../2xov/ .")
#     os.system("cp ../../2xov_strong_single_memory_600to500/simulation/"+str(i)+"/restart.2000000 2xov/")
#     os.system("run.py -s 4 -n 2 2xov/")
#     os.chdir("..")

# # rama_list = [6, 8, 16]
# # rama_list = [4]
# melt_t_list = [400, 500, 600]
# for variable in melt_t_list:
#     folder_name = str(variable)
#     os.system("mkdir "+folder_name)
#     os.chdir(folder_name)
#     os.system("cp -r ../1qjp .")
#     os.chdir("1qjp")
#     os.system(
#             "sed -i.bak 's/MELTT/'" +
#             str(variable) +
#             "'/g' 1qjp.in")
#     os.chdir("..")
#     # os.system("pwd")
#     os.system("run.py 1qjp/ -n 5 -s 5")
#     os.chdir("..")
# os.system("cp ~/opt/gg.py this_gg.py")
#
# exec (open("config.py").read())
# n = number_of_run
# steps = simulation_steps
#
# protein_name = args.protein.strip('/')
#
# temp = 400
# folder_name = "{}_t{}_q100_test11".format(protein_name, str(temp))
# print("all going to "+folder_name)
# os.system("mkdir -p "+folder_name)
# os.system("rm -f "+folder_name + "/*")
# command = 'cat simulation/{}/%d/wham11 \
# >> {}/all_wham.dat'.format(temp, folder_name)
# # cal rmsd
# os.chdir("simulation/"+str(temp))
# for i in range(n):
#     os.chdir(str(i))
#     os.system("awk '{print>\"file1\"(NR>(n/2)?2:1)}' n=\"$(wc -l <file1)\" file1")
#     os.system("cat file11 >> ../../../"+folder_name+"/rmsd_total")
#     # os.system("sed 1d wham.dat > wham1d.dat")
#     os.system("awk '{print>\"wham1\"(NR>(n/2)?2:1)}' n=\"$(wc -l <wham1)\" wham1")
#     os.chdir("..")
# os.chdir("../..")
# for i in range(n):
#     cmd = command % i
#     os.system(cmd)
# os.chdir(folder_name)
# os.system("awk '{print $2}' all_wham.dat > Qw_total")
# os.system("awk '{print $3}' all_wham.dat > rg_total")
# os.system("awk '{print $4}' all_wham.dat > p_total")
# os.system("awk '{print $5}' all_wham.dat > tc_total")
# os.system("awk '{print $NF}' all_wham.dat > e_total")
# os.system("cp ~/opt/wham_analysis/*.m .")
# os.chdir("..")
# os.system("~/opt/script/wham/fused_calc_cv.sc {} top7 50 400 350 450 5 50 100 0 0.98".format(folder_name))
#
#
# folder_name = "{}_t{}_q100_test12".format(protein_name, str(temp))
# print("all going to "+folder_name)
# os.system("mkdir -p "+folder_name)
# os.system("rm -f "+folder_name + "/*")
# command = 'cat simulation/{}/%d/wham12 \
# >> {}/all_wham.dat'.format(temp, folder_name)
# # cal rmsd
# os.chdir("simulation/"+str(temp))
# for i in range(n):
#     os.chdir(str(i))
#     os.system("cat file12 >> ../../../"+folder_name+"/rmsd_total")
#     os.chdir("..")
# os.chdir("../..")
# for i in range(n):
#     cmd = command % i
#     os.system(cmd)
# os.chdir(folder_name)
# os.system("awk '{print $2}' all_wham.dat > Qw_total")
# os.system("awk '{print $3}' all_wham.dat > rg_total")
# os.system("awk '{print $4}' all_wham.dat > p_total")
# os.system("awk '{print $5}' all_wham.dat > tc_total")
# os.system("awk '{print $NF}' all_wham.dat > e_total")
# os.system("cp ~/opt/wham_analysis/*.m .")
# os.chdir("..")
#
#
#
# os.system("~/opt/script/wham/fused_calc_cv.sc {} top7 50 400 350 450 5 50 100 0 0.98".format(folder_name))

#
# result_folder = "WeiLu_Aug_07"
# os.system("mkdir -p "+result_folder)
# protein_list = ['T089', 'T120', 'T251', 'top7', '1UBQ']
# # sublist = ['_ha', '_he']
# sublist = ['_lp', '_he_lp']
# folder_list = []
# for protein in protein_list:
#     for sub in sublist:
#         folder_list += [protein+sub]
# print(folder_list)
# # exit(1)
# # awk '{print>'file'(NR>(n/2)?2:1)}' n='$(wc -l <test)' test
# for folder in folder_list:
#     print(folder)
#     os.chdir(folder)
#     exec (open("config.py").read())
#     n = number_of_run
#     steps = simulation_steps
#     os.system("mkdir -p ../{}/".format(result_folder)+folder+"/best_q")
#     os.system("sort analysis/list_of_max_q > ../{}/q_".format(result_folder)+folder+".dat")
#     for i in range(n):
#         # move
#         os.chdir("analysis/"+str(i))
#         os.system("cp chosen.pdb ../../../{}/".format(result_folder) + folder+"/best_q/"+str(i)+".pdb")
#         os.chdir("../..")
#     os.chdir("..")


# result_folder = "WeiLu_Aug_07"
# os.system("mkdir -p "+result_folder)
# protein_list = ['T089', 'T120', 'T251', 'top7', '1UBQ']
# # sublist = ['_ha', '_he']
# sublist = ['_lp', '_he_lp']
# folder_list = []
# for protein in protein_list:
#     for sub in sublist:
#         folder_list += [protein+sub]
# print(folder_list)
# # exit(1)
#
# for folder in folder_list:
#     print(folder)
#     os.chdir(folder)
#     exec (open("config.py").read())
#     n = number_of_run
#     steps = simulation_steps
#     os.system("mkdir -p ../{}/".format(result_folder)+folder+"/best_q")
#     os.system("sort analysis/list_of_max_q > ../{}/q_".format(result_folder)+folder+".dat")
#     for i in range(n):
#         # move
#         os.chdir("analysis/"+str(i))
#         os.system("cp chosen.pdb ../../../{}/".format(result_folder) + folder+"/best_q/"+str(i)+".pdb")
#         os.chdir("../..")
#     os.chdir("..")
