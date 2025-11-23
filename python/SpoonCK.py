import shutil
import subprocess
import os
import pandas as pd

import ExcuteCK, ExcuteSpoon, getAllFile, getLog


def editClass(Spoonfile, CKfile, outPutFolder, fileName):
    df = pd.read_csv(CKfile)
    CK = df[["file", "class", "wmc", "tcc", "loc"]]
    CK["class"] = CK["class"].str.replace("$Anonymous", "$")
    spoon = pd.read_csv(Spoonfile)
    join = spoon.merge(CK, how="inner", on=["file", "class"])

    join.to_csv(
        outPutFolder + "/" + str(fileName) + "class.csv"
    ) 


def editMethod(SpoonFile, CKFile, outPutFolder, fileName):
    df = pd.read_csv(CKFile)
    CK = df[["file", "class", "method", "wmc", "loc"]]
    spoon = pd.read_csv(SpoonFile)
    join = spoon.merge(CK, how="inner", on=["file", "class", "method"])
    join.to_csv(
        outPutFolder + "/" + str(fileName) + "method.csv"
    )  # 後でフォルダ名を入力する


projectFolder = "C:/Users/sugii syuji/jsoup"            #input予定
outPutFolder = "C:/Users/sugii syuji/SpoonCK_data"      #input予定

absolutePath = os.getcwd()
tmpResult=absolutePath+"/tmpResult"
tmpCKClassResult=tmpResult+"/class.csv"
tmpCKMethodResult=tmpResult+"/method.csv"
tmpSpoonClassResult=tmpResult+"/spoonClass.csv"
tmpSpoonMethodResult=tmpResult+"/spoonMethod.csv"       #各ツールの結果を一時保存する場所，結合する必要あり
os.makedirs(tmpResult,exist_ok=True)            #一時保存するフォルダを作成

LogDir=absolutePath+"/logData"                  #ログのjava差分ファイル
LogFullDir=absolutePath+"/logFull"              #あるコミット時点の全てのjavaファイル
if os.path.isdir(LogFullDir):
    shutil.rmtree(LogFullDir)
os.makedirs(LogFullDir)

getLog.getLog(projectFolder,LogDir)
with open(LogDir+"/logHash.txt","r",encoding="utf-8") as f:
    hashList=[s.rstrip() for s in f.readlines()]

for i in range(5):
    hashSet=hashList[i]
    hashSplit=hashSet.split(",")
    DiffText=LogDir+"/"+hashSplit[0]+".txt"
    FullText=LogFullDir+"/"+hashSplit[0]+".txt"
    gitCheckout=["git","checkout",hashSplit[1]]
    subprocess.run(gitCheckout,cwd=projectFolder,check=True)
    getAllFile.searchFile(projectFolder,FullText)
    ExcuteCK.ExcuteCK(DiffText,tmpResult+"/")
    ExcuteSpoon.ExcuteSpoon(FullText,DiffText,tmpResult+"/")
    editClass(tmpSpoonClassResult,tmpCKClassResult,outPutFolder,i)
    editMethod(tmpSpoonMethodResult,tmpCKMethodResult,outPutFolder,i)