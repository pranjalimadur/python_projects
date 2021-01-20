import glob2
import datetime

file=glob2.glob("*.txt")

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt",'w') as fmerge:
    for f in file:
        with open(f,"r") as ff:
            fmerge.write(ff.read()+"\n")
