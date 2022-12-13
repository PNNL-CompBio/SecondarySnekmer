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
	mamba install -c conda-forge -c bioconda hhsuite 
