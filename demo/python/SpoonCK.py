import subprocess
import os
import pandas as pd


def editClass(Spoonfile, CKfile, outPutFolder, fileName):
    df = pd.read_csv(CKfile)
    CK = df[["file", "class", "wmc", "tcc", "loc"]]
    CK["class"] = CK["class"].str.replace("$Anonymous", "$")
    spoon = pd.read_csv(Spoonfile)
    join = spoon.merge(CK, how="inner", on=["file", "class"])

    join.to_csv(
        outPutFolder + "class" + str(fileName) + ".csv"
    )  # 後でフォルダ名を入力する


def editMethod(SpoonFile, CKFile, outPutFolder, fileName):
    df = pd.read_csv(CKFile)
    CK = df[["file", "class", "method", "wmc", "loc"]]
    spoon = pd.read_csv(SpoonFile)
    join = spoon.merge(CK, how="inner", on=["file", "class", "method"])
    join.to_csv(
        outPutFolder + "method" + str(fileName) + ".csv"
    )  # 後でフォルダ名を入力する


projectFolder = "C:/Users/syuuj/jsoup"
outPutFolder = "C:/Users/syuuj/SpoonCK_data/"
SpoonCMD = (
    "java -jar spoon/demo/target/demo-1.0-snapshot.jar "
    + projectFolder
    + " spoonCK_data/"
)
CkCMD = (
    "java -jar ck/target/ck-0.7.1-SNAPSHOT-jar-with-dependencies.jara "
    + projectFolder
    + " true 0 true spoonCK_data"
)

absolutePath = os.getcwd()

getCommitID = "git rev-list HEAD"
SpoonAnalyze = SpoonCMD.split()
CKAnalyze = CkCMD.split()

subprocess.run(["git", "checkout", "master"], cwd=projectFolder, check=True)
cp = subprocess.run(
    getCommitID.split(),
    encoding="utf-8",
    capture_output=True,
    text=True,
    cwd=projectFolder,
    check=True,
)

allCommitID = cp.stdout.split()
dataFolder = "spoonCK_data/class.csv"
CKData = ["class", "method", "field", "variable"]
for i in range(len(allCommitID)):
    commitID = allCommitID[i]
    subprocess.run(
        ["git", "checkout", "-f", commitID],
        cwd=projectFolder,
        encoding="utf-8",
        check=True,
    )
    subprocess.run(SpoonAnalyze, check=True, cwd=absolutePath)
    print(i)
    # subprocess.run(CKAnalyze,check=True,cwd=absolutePath)
    # editClass("spoonCK_data/spoonClass.csv","spoonCK_data/class.csv",outPutFolder,i+693)
    # editMethod("spoonCK_data/spoonMethod.csv","spoonCK_data/method.csv",outPutFolder,i+693)


string = subprocess.run(
    ["java", "-version"], capture_output=True, text=True, check=True
)
print(string.stderr)
