import os 
import subprocess

def ExcuteSpoon(full,diff,tmpResult):
    outPutDir=tmpResult    #結果を保存するフォルダ
    SpoonRootDir="C:\\Users\\sugii syuji\\spoonTEXT\\demo\\"

    spoonCMD=["java","-jar","target/demo-1.0-snapshot.jar",full,diff,outPutDir]
    subprocess.run(spoonCMD,check=True,cwd=SpoonRootDir)