import sys
sys.path.append("path/to/facebook-sdk-master") #this is the directory that facebook.py is in

#For extracting Images
import facebook
import urllib
import urllib3
import requests
#For extracting Tags
import http.client
import urllib.request
import urllib.parse
import urllib.error
import base64
import json
#For delay
import time

#Graph API user acces token
token = 'GRAPH_API_ACCESS_TOKEN'
#Microsoft Azure subscription key
subscription_key = 'AZURE_SUBSCRIPTION_KEY'
uri_base = 'westcentralus.api.cognitive.microsoft.com'

#Get from FB Graph API

graph = facebook.GraphAPI(access_token=token, version = '2.10')

albums = graph.request('FACEBOOK_PROFILE_NAME?fields=albums')
albumsList = albums['albums']
albumsDataList = albumsList['data']

#Get from Azure ML

headers = {
    # Request headers.
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': subscription_key,
}

params = urllib.parse.urlencode({
    # Request parameters. All of them are optional.
    'visualFeatures': 'Faces,Categories,Description,Color',
    'language': 'en',
})

#Search for Timeline Photos album
name = ''
num = -1
while name != 'Timeline Photos':
    num += 1
    album = albumsDataList[num]
    name = album['name']

timelineID = albumsDataList[num]['id']

timelineCount = graph.get_object(id=timelineID,fields='count')
count = timelineCount['count']

timelinePhotos = graph.get_object(id=timelineID,fields='photos.limit('+str(count)+')')
photos = timelinePhotos['photos']
photosList = photos['data']

index = 0

#First page
for i in range(len(photosList)):
    photoID = photosList[i]['id']
    
    #Getting URL of each image in first page
    photoInfo = graph.get_object(id=photoID,fields='images')
    picInfo = photoInfo['images']
    picture = picInfo[0]['source']
    
    #Getting date of each image in first page
    createdTime = photosList[i]['created_time']
    createdTime = createdTime[:16]
    createdTime = createdTime.replace('-','')
    createdTime = createdTime.replace('T','H')
    createdTime = createdTime.replace(':','M')
    
    #Getting likes of each image in first page
    likesInfo = graph.get_object(id=photoID+'/likes',summary='true')
    likesSummary = likesInfo['summary']
    likes = likesSummary['total_count']
    
    #Getting commentary number of each image
    commentsInfo = graph.get_object(id=photoID+'/comments',summary='true')
    commentsSummary = commentsInfo['summary']
    comments = commentsSummary['total_count']
    
    index += 1
    
    imageNum = "%05d" % index
    likesNum = "%06d" % likes
    commentsNum = "%05d" % comments
    
    url = picture
    
    #Saving image jpg
    filename = 'path/to/save/images/'+imageNum+'_'+createdTime+'_'+likesNum+'_'+commentsNum+'.jpg'
    imageDownload = urllib.request.urlretrieve(url,filename)
    
    #Saving tags txt
    body = "{'url':'"+url+"'}"

    conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()

    parsed = json.loads(data)
    result = json.dumps(parsed, sort_keys=True, indent=2)
    conn.close()
        
    tagsfilename = 'path/to/save/tags/'+imageNum+'_'+createdTime+'_'+likesNum+'_'+commentsNum+'.txt'        
    file = open(tagsfilename,'w')
    file.write(result)
    file.close()
    
    time.sleep(1)

#Repeat paging until final 100 images
for num in range(count//100):
    
    #Accessing next page
    paging = photos['paging']
    cursors = paging['cursors']
    after = cursors['after']

    nextPage = graph.get_object(id=timelineID,fields='photos.after('+str(after)+').limit('+str(count)+')')
    photos = nextPage['photos']
    photosList = photos['data']

    #i=position of photo being extracted
    for i in range(len(photosList)):
        photoID = photosList[i]['id']

        #Getting URL of each image
        photoInfo = graph.get_object(id=photoID,fields='images')
        picInfo = photoInfo['images']
        picture = picInfo[0]['source']
        
        #Getting date of each image
        createdTime = photosList[i]['created_time']
        createdTime = createdTime[:16]
        createdTime = createdTime.replace('-','')
        createdTime = createdTime.replace('T','H')
        createdTime = createdTime.replace(':','M')
        
        #Getting likes of each image
        likesInfo = graph.get_object(id=photoID+'/likes',summary='true')
        likesSummary = likesInfo['summary']
        likes = likesSummary['total_count']
        
        #Getting commentary number of each image
        commentsInfo = graph.get_object(id=photoID+'/comments',summary='true')
        commentsSummary = commentsInfo['summary']
        comments = commentsSummary['total_count']
        
        index += 1
        
        imageNum = "%05d" % index
        likesNum = "%06d" % likes
        commentsNum = "%05d" % comments

        url = picture
        
        #Saving image jpg
        filename = 'path/to/save/images/'+imageNum+'_'+createdTime+'_'+likesNum+'_'+commentsNum+'.jpg'
        imageDownload = urllib.request.urlretrieve(url,filename)\
        
        #Saving tags txt
        body = "{'url':'"+url+"'}"
        
        conn = http.client.HTTPSConnection('westcentralus.api.cognitive.microsoft.com')
        conn.request("POST", "/vision/v1.0/analyze?%s" % params, body, headers)
        response = conn.getresponse()
        data = response.read()

        parsed = json.loads(data)
        result = json.dumps(parsed, sort_keys=True, indent=2)
        conn.close()

        tagsfilename = 'path/to/save/tags/'+imageNum+'_'+createdTime+'_'+likesNum+'_'+commentsNum+'.txt'        
        file = open(tagsfilename,'w')
        file.write(result)
        file.close()

        time.sleep(1)
