import os
import subprocess

def ExcuteCK(gitDiffFile,tmpResult):
    CKrootDir="C:\\Users\\sugii syuji\\CKTEXT\\ck" #ckツールのルートディレクトリ
    outPutDir=tmpResult

    CkCMD=["java","-jar","target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jar",gitDiffFile,"false","0","true",outPutDir]
    subprocess.run(CkCMD,check=True,cwd=CKrootDir)

