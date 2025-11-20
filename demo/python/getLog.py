import subprocess
import os
import shutil


def getLog(rootProject):
    gitProject = rootProject
    saveLogDir = "logData"

    if os.path.isdir(saveLogDir):
        shutil.rmtree(saveLogDir)
    os.makedirs(saveLogDir)

    beLatestVersion = "git checkout master"
    subprocess.run(beLatestVersion.split(), cwd=gitProject, check=True)

    getLog = "git log --pretty=format:%H --name-only -- *.java"
    hash = subprocess.run(
        getLog.split(), cwd=gitProject, capture_output=True, check=True, text=True
    )
    list = hash.stdout.split("\n\n")
    k = 0
    for commit in list:
        commit = commit.split("\n")
        newList = [i for i in commit if "test" not in i and "info" not in i]
        for i in range(1, len(newList)):
            newList[i] = gitProject + "/" + newList[i]
        fileWrite = "\n".join(newList)
        if len(newList) >= 2:
            k = k + 1
            with open(saveLogDir + "/" + str(k) + ".txt", "w", encoding="utf-8") as f:
                f.write(fileWrite)


# gitプロジェクトのパスから、test info を除いた Javaファイル を変更したlog( commitID と　変更Javaファイル )をlogDataに保存する　※１つのコミットに対して１つのファイル
