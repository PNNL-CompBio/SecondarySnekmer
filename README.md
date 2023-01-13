# SecondarySnekmer
The files necessary to run the Porter 5 and Snekmer Docker container.

This is a repository for the Docker combination tool between Secondary Structure/Porter 5 and Snekmer.
This is meant for users to be able to quickly run a single command or two that will be able to automatically
run the programs Porter5 and Snekmer in succession with any data that they wish to use.

This program must be run on a Linux system, as secondary structure will not work on windows devices due to the
required tool HHBlits.

To run this program docker must be installed on your device. This can be done by following the steps on this
website: https://docs.docker.com/engine/install/. Docker desktop for windows does exist but it will not allow
this program to run correctly.

Once this is done, place the Dockerfile into a separate directory from your main files. I would suggest in a 
folder titled myimages or dockerfileImages. Once this is done, initialize the image using the command 
'docker build -t secondSnekmer .'. This command must be run while in the same directory as the dockerfile. You will know
if the image was built correctly if you use the command 'docker images' and the repository secondSnekmer is shown with a
size of 4.04 GB. 

Currently the Dockerfile does not install Uniprot on its own to run with secondary structure/Porter 5. This will
need to be downloaded separately and a python file is being written to automatically download and install the uniprot
file into a given directory when initializing the docker container.

To allow the docker container to have access to the installed Uniprot directory (as the directory is over 30 GB),
use the command 'docker run -v [current working directory/path]/uniprot20_2016_02:/uniprot20_2016_02 -it secondSnekmer'. This
will create the directory uniprot20_2016_02 in the folder for Secondary Structure to use.

These files are the edited files originally contained with Porter 5 as well as extra code necessary to allow porter 5 and snekmer to work in the same container.
To set up Porter5, run the shell script porterSetup.sh when entering the container. This will negate the need for setup when running porter5/secondary structure for the first time.

Before running Porter5 and Snekmer in the container, several steps must be done before running the program.

QUICK SETUP:

To automatically skip step 1 and also install the docker container along with setting up the container to immediately run Porter5, run ‘python SSnekmerDocker.py’ before continuing on with the following steps. 

To automatically run Porter5 and Snekmer one after the other without having to follow the steps, after running SSnekmerDocker.py and starting the container run “python SecStructSnekmer.py [fasta file location]” to automatically be able to skip steps 2-10. 


Step 1: Place all of the replacement Porter5 code in the SecondarySnekmer folder (multi_fasta.py, split_fasta.py, etc) into the Porter5 folder. These need to replace the original Porter5 code located there.

Step 2: Split the fasta files or other files into single-line files using the split_fasta.py code by using the command 'python split_fasta.py [large Fasta file location]'. This will create a directory in the same folder as the large fasta file containing the new split fasta files and named after the original fasta file.

Step 2.5: If multiple large fasta files need to be split, run the command 'python runPorterMultiple.py [fasta files location]'. This will split all of the fasta files within the directory and then run 'multiple_fasta.py' without needing user input.

Step 3: Once the file has been split, run 'python multiple_fasta.py [new directory made in step 2]' to get the final results from the secondary structure analysis.

Step 4: To get the SS3 and SS8 files needed to run snekmer with the results from the secondary structure analysis, run 'python combineSecondary.py [directory location of results]'. The results directory location should be the same location as the original split fasta files; this will go through the files and combine them all back into a single SS3 or SS8 file for every original fasta file split during split_fasta.py or runPorterMultiple.py. The final file will be called [fasta name]ss8.fasta or [fasta name]ss3.fasta. 

Step 5: Copy all ss3 fasta files into one folder for snekmer analysis and all ss8 fasta files into another folder for snekmer analysis. 

Step 6: Copy the ss3 folder to the main directory and rename the folder to 'input'.

Step 7: Copy the file 'config.yaml' from Snekmer/resources and place it in the main directory.

Step 8: Run the command 'snekmer model --configfile config.yaml' to run Snekmer. The results will be located in the output folder.

Step 9: Zip or rename the output folder to 'results_[time]_[fastaName]_ss3'

Step 10: Repeat steps 6-9 for the ss8 directory and files.
