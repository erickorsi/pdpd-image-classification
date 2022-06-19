#-----Create File "All_Dict.txt" : All information on each image-----

import matplotlib.pyplot as plt
import numpy as np
import os
import re
import json
import csv
import ast

dictIndexAll = {}

for dirname, dirnames, filenames in os.walk('path/to/tags'):

    for filename in filenames:
        dictInfo = {}
        dateInfo = {}
        #print (filename)

        #---image data (Facebook)---

        # creating variables
        infos = re.split("_",filename)
        index = int(infos[0])
        date = infos[1]
        likes = int(infos[2])
        infos2 = re.split("\.",infos[3])
        comments = int(infos2[0])
        time = date.replace("M",":")
        time = time[-5:]
        hour = int(time[:2])
        minute = int(time[-2:])
        newdate = date[:8]
        day = int(newdate[6:8])
        month = int(newdate[4:6])
        year = int(newdate[:4])

        # inserting variables in dictionary
        dateInfo["year"] = year
        dateInfo["month"] = month
        dateInfo["day"] = day
        dateInfo["hour"] = hour
        dateInfo["minute"] = minute
        dictInfo["date"] = dateInfo
        dictInfo["likes"] = likes
        dictInfo["comments"] = comments

        #---visual elements of image (Azure)---
        directory = "path/to/tags/"+filename

        # getting file dictionary
        file = open(directory,'r')        
        fileString = file.read()
        fileDict = json.loads(fileString)
        file.close()

        # creating variables
        listCategories = fileDict["categories"]
        dictDescription = fileDict["description"]
        dictCaptions = dictDescription["captions"][0]
        listTags = dictDescription["tags"]

        # inserting variables in dictionary
        dictInfo["categories"] = listCategories
        dictInfo["captions"] = dictCaptions
        dictInfo["tags"] = listTags

        dictIndexAll[index] = dictInfo

#Directory name
filename = "path/to/save/All_Dict.txt"
file = open(filename,"w+")
string = str(dictIndexAll)
result = json.dumps(string, sort_keys=True, indent=2)
file.write(result)
file.close()

#-----Creating File "Tags_List.txt" : list of all possible tags in sample-----

tagsList = []

for index,info in dictIndexAll.items():
    indexInfo = dictIndexAll[index]
    imageDate = indexInfo['date']
    imageLikes = indexInfo['likes']
    imageComments = indexInfo['comments']
    imageTags = indexInfo['tags']
    
    for tag in imageTags:
        if tag not in tagsList:
            tagsList.append(tag)

#Directory name
filename = "path/to/save/Tags_List.txt"
file = open(filename,'w+')

for tag in tagsList:
    if tag==tagsList[0]:
        file.write(tag)
    else:
        file.write(";"+tag)
file.close()

#-----Creating File "Bivariate_Table.csv" : the organized dataset for machine learning application -----

#Importing the previous files, in case the code is modulary.

directory = "path/to/All_Dict.txt"
file = open(directory,'r')        
fileString = file.read()
String_Geral = json.loads(fileString)
file.close()

tagsList = []
directory2 = "path/to/Tags_List.txt"
Dict_Geral = ast.literal_eval(String_Geral)
file2 = open(directory2,'r')
reader = file2.read()
tagsList = reader.split(";")
file2.close()

#---
bivariadaInfo = {}

#Directory name
filename = "path/to/save/Bivariate_Table.csv"
file = open(filename,'w+')

file.write("index")
for tag in tagsList:
    file.write(";"+tag)
file.write(";likes")

for index,info in Dict_Geral.items():
    indexInfo = Dict_Geral[index]
    imageDate = indexInfo['date']
    imageLikes = indexInfo['likes']
    imageComments = indexInfo['comments']
    imageTags = indexInfo['tags']
    imgInfo = {}
    tagsInfo = []
    
    file.write("\n"+str(index))
    for tag in tagsList:
        if tag in imageTags:
            file.write(";"+"1")
            tagsInfo.append(1)
        else:
            file.write(";"+"0")
            tagsInfo.append(0)
        i+=1
    file.write(";"+str(imageLikes))
    imgInfo["tags"] = tagsInfo
    imgInfo["likes"] = imageLikes
    bivariadaInfo[index] = imgInfo
            
file.close()

#-----Creating File "Bivariate_Info.txt" : text version of dataset-----

#Directory name
filename = "path/to/save/Bivariate_Info.txt"
file = open(filename,"w+")
string = str(bivariadaInfo)
result = json.dumps(string, sort_keys=True, indent=2)
file.write(result)
file.close()

#-----Creating boxplot of tags-----

def create_boxplot():
    '''
    Create Boxplot for a single tag.
    '''
    directory = "path/to/Bivariate_Info.txt"
    file = open(directory,'r')        
    fileString = file.read()
    String_Geral = json.loads(fileString)
    file.close()
    bivariadaInfo = ast.literal_eval(String_Geral)

    num1 = 0
    num0 = 0
    likesList0 = []
    likesList1 = []

    for index,info in bivariadaInfo.items():
        tags = info['tags']
        likes = info['likes']
        if tags[0]==0:
            num0+=1
            likesList0.append(likes)
        if tags[0]==1:
            num1+=1
            likesList1.append(likes)

    data = [likesList0,likesList1]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.boxplot(data,showmeans=True)
    ax.set_xticklabels(['0', '1'])

    plt.show()

    #Without outliers

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.boxplot(data, 0, '',showmeans=True)
    ax.set_xticklabels(['0', '1'])

    plt.show()