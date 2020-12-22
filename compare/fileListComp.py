import os 

# 获取指定文件夹的列表
def check_file(file_path):
    all_file = os.listdir(file_path)
    files = []
    for f in all_file:
        if os.path.isdir(os.path.join(file_path,f)):
            files.extend(check_file(os.path.join(file_path,f)))
        elif f==".DS_Store":
            continue
        else:
            files.append(f)
    return files
# 比较文件列表
def comareFileList(dir_1, dir_2):
    fileSet1=set(check_file(dir_1))
    fileSet2=set(check_file(dir_2))
    print(len(fileSet1))
    print(len(fileSet2))
    if len(fileSet1)>len(fileSet2):
        return list(fileSet1-fileSet2)
    else:
        return list(fileSet2-fileSet1)
if __name__=="__main__":
    pwd=os.getcwd()
    print(pwd)
    os.chdir("/Users/huan/Desktop")
    fileList=comareFileList("imgfakelabel/否", "no-筛选")
    print(fileList)
    print(len(fileList))
