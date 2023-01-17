import os

#directoryPath should be where the inputted fasta files are being stored. This will only use fasta files with a name ending in .fa or .fasta.
def runPorterMultiple(directoryPath):
    fileList = os.listdir(directoryPath)
    for f in fileList:
        print(f)
        f_full = directoryPath+"/"+f
        if f.endswith(".fa") or f.endswith(".fasta"):
            #splitting the fasta files into separate 1 line files in a folder renamed after the original fasta file
            oscommand = "python Porter5/split_fasta.py " +f_full+" --cpu 4 --fast"
            os.system(oscommand)
            
    #using the created folders to run multiple_fasta.py from Porter5 for each new folder.
    subfolders = [ f.path for f in os.scandir(directoryPath) if f.is_dir() ]
    print(subfolders)
    for folder in subfolders:
        oscommand = "python Porter5/multiple_fasta.py -i "+folder+" --cpu 4 --fast"
        os.system(oscommand)

