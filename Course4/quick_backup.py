#! python
import subprocess
import os
from multiprocessing import Pool

src = "/home/student-01-14ada6df1709/data/prod"
dest = "/home/student-01-14ada6df1709/data/prod_backup"

def run(dir):
    subprocess.call(["rsync", "-arq", dir, dest])

if __name__ == "__main__":
    filePaths = [os.path.join(src,f) for f in os.listdir(src)]
    P = Pool(len(filePaths))
    P.map(run, filePaths)


/home/student-02-81f317e4a400/images