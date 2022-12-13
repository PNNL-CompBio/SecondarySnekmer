import os
import glob
import numpy
from pathlib import Path
import pathlib
import pandas as pd

def combineSecondary(rootdirectory):
    rootdir = rootdirectory
    subfolders = [f.path for f in os.scandir(rootdir) if f.is_dir()]
    for subdir in subfolders:
        print(subdir)
        pathFolder = pathlib.PurePath(subdir)
        dname = pathFolder.name
        print(dname)
        if not 'folder' in dname:
            ss3names = []
            ss8names = []
            resultSs3 = []
            resultSs8 = []

            for file in os.listdir(subdir):
                if file.endswith('.ss3'):
                    ss3names.append(Path(file).stem)
                    fullPath = subdir + "/" + Path(file).stem + ".ss3"
                    X = pd.read_csv(fullPath, sep="\t", header=None)
                    ss3 = ''.join(X[2][2:].tolist())
                    resultSs3.append(ss3)
                    #f=open(fullPath,"r")
                    #lines=f.readlines()
                    #for x in lines:
                        #	resultSs3.append(x.split('\t')[2])
                    #f.close()
            for file in os.listdir(subdir):
                if file.endswith('.ss8'):
                    ss8names.append(Path(file).stem)
                    fullPath = subdir + "/" + Path(file).stem + ".ss8"
                    X = pd.read_csv(fullPath, sep="\t", header=None)
                    ss8 = ''.join(X[2][2:].tolist())
                    resultSs8.append(ss8)
                    #f=open(fullPath,"r")
                    #lines=f.readlines()
                    #for x in lines:
                    #	resultSs8.append(x.split('\t')[2])
                    #f.close()

            fastaNameSs3 = dname + "ss3.fasta"
            ofile = open(fastaNameSs3, "w")

            for i in range(len(ss3names)):

                ofile.write(">" + ss3names[i] + "\n" + (resultSs3[i]) + "\n")

    #do not forget to close it

            ofile.close()

            fastaNameSs8 = dname + "ss8.fasta"
            ofile = open(fastaNameSs8, "w")

            for i in range(len(ss8names)):

                ofile.write(">" + ss8names[i] + "\n" + (resultSs8[i]) + "\n")

    #do not forget to close it

            ofile.close()