import requests
import csv
from xml.dom import minidom

# Connect the URL to get the trin information
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

retrieveTags=['TrainStatus', 'TrainLatitude', 'TrainLongitude', 'TrainCode', 'TrainDate', 'PublicMessage', 'Direction' ] 

# Using mini dom ge the Train information
doc = minidom.parseString(page.content) 
# check it works 
# print (doc.toprettyxml())
# Write the file in to xml
with open("trainxml.xml","w") as xmlfp: 
    doc.writexml(xmlfp) 

with open("train.csv","w") as train_file:
    trainwriter =  csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL) 

    # get the train object
    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions") 
    for objTrainPositionsNode in objTrainPositionsNodes:     
        # From train object get the train code 
        traincode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)   
        #Check Trincode Start with "D"     
        if traincode.firstChild.nodeValue.strip().startswith("D"):
            dataList = [] 
            # Retrive the data and store in to CSV
            for retrieveTag in retrieveTags: 
                datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0) 
                dataList.append(datanode.firstChild.nodeValue.strip()) 
            trainwriter.writerow(dataList)   