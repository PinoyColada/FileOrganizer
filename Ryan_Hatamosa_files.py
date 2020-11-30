"""
Author:Ryan Hatamosa
"""

import os, shutil, gzip

dirList = ["SampleData", "folder1", "folder12", "folder11", "folder111", "folder1111"]
csvList = ["dataframe01.csv", "dataframe11.csv"]
imageList = ["image111.jpg", "image112.jpg"]
imagesAndTextList = ["image1111.jpg", "image1112.jpg", "textFile1111.txt"]
imageList2 = ["image11111.jpg", "image11112.jpg", "image11113.jpg", "image11114.jpg"]
dirPath = r"C:\Users\Ryan Hatamosa\Desktop\Documents"
dirPath = os.path.join(dirPath, "Ryan_Hatamosa_DIR")
os.makedirs(dirPath)  # creating Ryan_Hatamosa_DIR in Documents directory

def phase1(dirList,csvList,imageList,imagesAndTextList,imageList2,dirPath):

    for i in dirList:
        print("Creating", i, "in Ryan_Hatamosa_DIR...")
        path = os.path.join(dirPath, i)
        os.mkdir(path)
        print(i, "created!")
        print("---------------------------")

        if i == dirList[1] or i == dirList[2]:
            if i == dirList[1]:
                csvName = csvList[0]
            elif i == dirList[2]:
                csvName = csvList[1]
            print("Creating", csvName, "in", dirPath)
            with open('{file_path}'.format(file_path=os.path.join(dirPath, csvName)), 'w') as f:
                pass
                f.close()
            print(csvName, "created!")
            print("---------------------------")
        elif i == dirList[3] or i == dirList[4] or i == dirList[5]:
            if i == dirList[3]:
                choice = imageList
            elif i == dirList[4]:
                choice = imagesAndTextList
            elif i == dirList[5]:
                choice = imageList2
            for j in choice:
                print("Creating", j, "in", path)
                with open('{file_path}'.format(file_path=os.path.join(path, j)), 'w') as f:
                    pass
                    f.close()
                print(j, "created!")
                print("---------------------------")

        if i == dirList[2]:
            continue
        else:
            dirPath = path


def phase2():
    print("Replicating content of Ryan_Hatamosa_DIR to new directory Ryan_Hatamosa_DIR-CP...")
    shutil.copytree(r"C:\Users\Ryan Hatamosa\Desktop\Documents\Ryan_Hatamosa_DIR",
                r"C:\Users\Ryan Hatamosa\Desktop\Documents\Ryan_Hatamosa_DIR-CP")
    print("Replication successful!")
    print("---------------------------")

def phase3(dirPath):
    dirPath2 = r"C:\Users\Ryan Hatamosa\Desktop\Documents\Ryan_Hatamosa_DIR-CP"
    dirPath3 = dirPath2
    dirPath4 = dirPath
    dirPath5 = dirPath

    print("Going through Ryan_Hatamosa_DIR and deleting all .txt files...")
    for i in dirList:
        if i == dirList[2]:
            continue
        else:
            dirPath = os.path.join(dirPath, i)
            test = os.listdir(dirPath)
            for item in test:
                if item.endswith(".txt"):
                    os.remove(os.path.join(dirPath, item))
    print("Deletion successful!")
    print("---------------------------")

    print("Renaming all files with names ending in '2.jpg' with '2.pdf' in Ryan_Hatamosa_DIR-CP...")
    for i in dirList:
        if i == dirList[2]:
            continue
        else:
            dirPath2 = os.path.join(dirPath2, i)
            test = os.listdir(dirPath2)
            for item in test:
                if item.endswith("2.jpg"):
                    name = os.path.join(dirPath2, item)
                    altered = name.replace('.jpg','.pdf')
                    os.rename(name,altered)
    print("Renaming successful!")
    print("---------------------------")

    print("Getting all pdf files and archiving them into the 'pdf2.gzip'... Also moving it to Ryan_Hatamosa_DIR...")
    for i in dirList:
        if i == dirList[2]:
            continue
        else:
            dirPath3 = os.path.join(dirPath3, i)
            test = os.listdir(dirPath3)
            for item in test:
                if item.endswith(".pdf"):
                    f_in = open(os.path.join(dirPath3 + '\\' + item))
                    f_out = gzip.open(dirPath5 + '\\pdf2.gzip', 'wb')
                    f_out.writelines(f_in)
                    f_out.close()
                    f_in.close()
    print("All pdf files are archived into 'pdf2.gzip' and moved to Ryan_Hatamosa_DIR!")
    print("---------------------------")

    print("Creating a file named 'listofall.txt' of all information from Ryan_Hatamosa_DIR-CP before" +
          "deleting the directory and moving listofall.txt to Ryan_Hatamosa_DIR...")
    alltxt_cp = open(dirPath4 + "\\" + "listofall.txt", "w")
    for path, subdirs, files in os.walk(r'C:\Users\Ryan Hatamosa\Desktop\Documents\Ryan_Hatamosa_DIR-CP'):
        for filename in files:
            f = os.path.join(path, filename)
            alltxt_cp.write(str(f) + os.linesep)
    shutil.rmtree(r"C:\Users\Ryan Hatamosa\Desktop\Documents\Ryan_Hatamosa_DIR-CP")
    print("All information from Ryan_Hatamosa_DIR-CP has been moved into listofall.txt inside Ryan_Hatamosa_DIR" +
          "and Ryan_Hatamosa_DIR-CP has been completely deleted!")
    print("---------------------------")

def phase4():
    print("Creating a Backup folder in Download directory and" +
          "storing both listofall.txt & pdf2.gzip in the folder...")
    newBackUpFolder = (r"C:\Users\Ryan Hatamosa\Downloads")
    newBackUpFolder = os.path.join(newBackUpFolder,"Backup")
    backUp1 = r"C:\Users\Ryan Hatamosa\Desktop\Documents\Ryan_Hatamosa_DIR\listofall.txt"
    backUp2 = r"C:\Users\Ryan Hatamosa\Desktop\Documents\Ryan_Hatamosa_DIR\pdf2.gzip"
    shutil.copyfile(backUp1,newBackUpFolder)
    shutil.copyfile(backUp2,newBackUpFolder)
    print("Successfully created Backup folder in Download directory and stored listofall.txt & pdf2.gzip inside it!")
    print("---------------------------")

def phase5():
    print(" ")
    print("VISUAL REPRESENTATION OF")
    print("  Ryan_Hatamosa_DIR  ")
    print("-------------------------")
    print("SampleData/")
    print("|--dataframe01.csv")
    print("|--folder1")
    print("|  |--dataframe11.csv")
    print("|  |--folder11")
    print("|  |  |--folder111")
    print("|  |  |  |--folder1111")
    print("|  |  |  |  |--image11111.jpg")
    print("|  |  |  |  |--image11112.jpg")
    print("|  |  |  |  |--image11113.jpg")
    print("|  |  |  |  |--image11114.jpg")
    print("|  |  |  |--image1111.jpg")
    print("|  |  |  |--image1112.jpg")
    print("|  |  |--image111.jpg")
    print("|  |  |--image112.jpg")
    print("|  |--folder12")
    print("|--listofall.txt")
    print("|--pdf2.gzip")


if __name__ == '__main__':
    phase1(dirList,csvList,imageList,imagesAndTextList,imageList2,dirPath)
    phase2()
    phase3(dirPath)
    phase4()
    phase5()
