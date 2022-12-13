import os

def runPorterMultiple(directoryPath):
    fileList = os.listdir(directoryPath)
    for f in fileList:
        print(f)
        f_full = directoryPath+"/"+f
        if f.endswith(".fa") or f.endswith(".fasta"):
            oscommand = "python Porter5/split_fasta.py " +f_full+" --cpu 4 --fast"
            os.system(oscommand)

    subfolders = [ f.path for f in os.scandir(directoryPath) if f.is_dir() ]
    print(subfolders)
    for folder in subfolders:
        oscommand = "python Porter5/multiple_fasta.py -i "+folder+" --cpu 4 --fast"
        os.system(oscommand)

