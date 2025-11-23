import os

def searchFile(ROOT_PATH,saveFile):
    with open (saveFile,"w") as f:
        for pathname,dirnames,filenames in os.walk(ROOT_PATH):
            for filename in filenames:
                if filename.endswith(".java"):
                    fullPath=os.path.join(pathname,filename)
                    if "test" not in fullPath and "info" not in fullPath :
                        print(fullPath,file=f)
                     

#gitProject="C:\\Users\\sugii syuji\\jsoup"
#searchFile(gitProject)

#gitプロジェクトのパスを渡して、gitプロジェクト内に含まれる test info を除いたjavaファイルの一覧を取得する