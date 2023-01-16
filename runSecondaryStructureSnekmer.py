#Use SS3 and SS8 Results with Snekmer

#Please input the folder that the .SS3 results from Porter5 reside in.

import sys
import os
import runPorterMultiple
import combineSecondary

fileLoc = sys.argv[1]

print("This will not function if Porter5 is not set up. Please make sure Porter5 is set up using the command python3 Porter5 --setup.")
print("Please make sure that the folder name used is the full folder path.")
print(fileLoc)

print("This is your file location for your files to run with both secondary structure and snekmer.\t")

runPorterMultiple.runPorterMultiple(fileLoc)

combineSecondary.combineSecondary(fileLoc)

#os.system("rm -r input")

os.system("mkdir input")

os.system("cp *ss3.fasta input")

os.system("cp Snekmer/resources/config.yaml config.yaml")

print("Running Snekmer analysis on SS3 results")

os.system("snekmer model")

os.system("cp -r output outputSS3")

os.system("rm -r output")

os.system("rm -r input")

os.system("mkdir input")

os.system("cp *ss8.fasta input")

print("Running Snekmer analysis on SS8 results")

os.system("snekmer model")

os.system("cp -r output outputSS8")

os.system("rm -r output")
#this needs to take the location given for use with snekmer as the input folder.
#the input should be the ss3 and ss8 files given from secondary structure.
