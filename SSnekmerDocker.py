import subprocess
import sys
import os
import glob
import shutil

if not os.path.exists("myimages"):
    subprocess.call(["mkdir", "myimages"])

else:
    shutil.rmtree("myimages")
    subprocess.call(["mkdir", "myimages"])

subprocess.call(["cp", "Dockerfile", "myimages/Dockerfile"])

#THIS STEP WILL TAKE A LONG TIME
subprocess.call(["wget", "http://wwwuser.gwdg.de/~compbiol/data/hhsuite/databases/hhsuite_dbs/old-releases/uniprot20_2016_02.tgz"])

subprocess.call(["cd", "myimages"])

subprocess.call(["docker", "build", "-t", "SSnekmer", "."])

#check at this step to see if the docker image was built correctly using 'docker images'

CWD = os.getcwd()

uniLoc = CWD + "uniprot20_2016_02:/uniprot20_2016_02"

secStructLoc = CWD + "secStruct.py:/secStruct.py"

combineLoc = CWD + "combineSecondary.py:/combineSecondary.py"

runPorterMultLoc = CWD + "runPorterMultiple.py:/runPorterMultiple.py"

splitFastaLoc = CWD + "split_fasta.py:/split_fasta.py"

subprocess.call(["cd","../"])

subprocess.call(["docker","run","-v",uniLoc,"-v",secStructLoc,"-v",combineLoc,"-v",runPorterMultLoc,"-v",splitFastaLoc,"-it","SSnekmer"])

#docker run -v /home/schm285/uniprot20_2016_02:/uniprot20_2016_02 -v /home/schm285/secStruct.py:/secStruct.py -v /home/schm285/combineSecondary.py:/combineSecondary.py -v /home/schm285/runPorterMultiple.py:/runPorterMultiple.py -v/home/schm285/split_fasta.py:split_fasta.py -it hh_test