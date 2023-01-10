FROM condaforge/mambaforge:latest AS mambasetup

ENV DEBIAN_FRONTEND = noninteractive

RUN git clone https://github.com/PNNL-CompBio/Snekmer.git && \
	mamba env update -n base -f ./Snekmer/environment.yml && \
	pip install opencv-python && \
	apt update && apt install -y libsm6 libxext6 && \
	apt-get install -y libxrender-dev && \
	pip install Snekmer/. && \
	git clone https://github.com/mircare/Porter5/ --depth 1 && rm -rf Porter5.git && \
	apt-get install -y build-essential && \
	mamba install -c conda-forge -c bioconda hhsuite && \
        git clone https://github.com/DarrenJSchmidt/SecondarySnekmer.git

RUN echo "Run the command docker run -v [working directory]/uniprot20_2016_02:/uniprot20_2016_02 -it [image] where working directory is the directory where the uniprot file is stored. This will be necessary for running secondary structure."
