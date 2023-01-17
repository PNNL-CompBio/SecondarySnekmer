import subprocess
import sys
import os
import glob
import shutil

#removing the folder myimages if it exists and creating an empty myimages folder. Make sure that there are no files that you want to keep in myimages beforehand.

if not os.path.exists("myimages"):
    subprocess.call(["mkdir", "myimages"])

else:
    shutil.rmtree("myimages")
    subprocess.call(["mkdir", "myimages"])

#Copying the dockerfile to a set location (the myimages folder)

subprocess.call(["cp", "Dockerfile", "myimages/Dockerfile"])

#THIS STEP WILL TAKE A LONG TIME
subprocess.call(["wget", "http://wwwuser.gwdg.de/~compbiol/data/hhsuite/databases/hhsuite_dbs/old-releases/uniprot20_2016_02.tgz"])

#changing the local destination to myimages to build the Dockerfile

subprocess.call(["cd", "myimages"])

subprocess.call(["docker", "build", "-t", "SecondarySnekmer", "."])

#check at this step to see if the docker image was built correctly using 'docker images'

CWD = os.getcwd()

uniLoc = CWD + "uniprot20_2016_02:/uniprot20_2016_02"

secStructLoc = CWD + "secStruct.py:/secStruct.py"

combineLoc = CWD + "combineSecondary.py:/combineSecondary.py"

runPorterMultLoc = CWD + "runPorterMultiple.py:/runPorterMultiple.py"

splitFastaLoc = CWD + "split_fasta.py:/split_fasta.py"

#switching the folder location back to the original destination

subprocess.call(["cd","../"])

#opening the Docker container

subprocess.call(["docker","run","-v",uniLoc,"-v",secStructLoc,"-v",combineLoc,"-v",runPorterMultLoc,"-v",splitFastaLoc,"-it","SecondarySnekmer"])

#docker run -v /home/schm285/uniprot20_2016_02:/uniprot20_2016_02 -v /home/schm285/secStruct.py:/secStruct.py -v /home/schm285/combineSecondary.py:/combineSecondary.py -v /home/schm285/runPorterMultiple.py:/runPorterMultiple.py -v/home/schm285/split_fasta.py:split_fasta.py -it hh_test
