import os

gitLogFile="C:\\Users\\syuuj\\spoonTEXT\\demo\\logData\\20.txt"
with open(gitLogFile,"r",encoding="UTF-8") as f:
    script=f.read()
    
files=[i for i in script.split() if os.path.isfile(i)]
CkCMD=["java","-jar","ck/target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar","","false","0","true",""]
for file in files:
    CkCMD[3]=file
    print(" ".join(CkCMD))
