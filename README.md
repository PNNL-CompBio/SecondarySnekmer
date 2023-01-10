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
