#Test is not an active file - this is only to set up Porter5
#!/bin/sh
echo "psiblast" "uniref90" "hhblits" "uniprot20_2016_02/uniprot20_2016_02" | xargs -n 1 echo | python3 Porter5/Porter5.py -i Porter5/example/2FLGA.fasta --cpu 2 --fast --setup

