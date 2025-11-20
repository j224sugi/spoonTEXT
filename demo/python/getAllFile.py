import os

def serchFile(ROOT_PATH):
    with open ("first.txt","w") as o:
        for pathname,dirnames,filenames in os.walk(ROOT_PATH):
            for filename in filenames:
                if filename.endswith(".java"):
                    fullPath=os.path.join(pathname,filename)
                    if "test" not in fullPath and "info" not in fullPath :
                        print(fullPath,file=o)
                     

gitProject="C:\\Users\\syuuj\\jsoup"
serchFile(gitProject)

#gitプロジェクトのパスを渡して、gitプロジェクト内に含まれる test info を除いたjavaファイルの一覧を取得する