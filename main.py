###########################################
#
#               Python API                
#
#               by Jimmi Lin
#
#
###########################################

import requests
import json
import csv


## API key and uid for accessing form information
key = "ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d"
uid = "PfSNFM"

## list for future use

##x-axis header
data_header = list()
##question id for identifying response
question_id = list()


## url for request
url = "https://api.typeform.com/v1/form/" + uid + "?key=" + key


##sending request for response
resp = requests.get(url)
data = resp.json()




##check if connection is fine          
if data['http_status'] == 200:
    ##open file for writing
    write_data = open('.\data.csv', 'w', encoding='UTF-8')
    data_writer = csv.writer(write_data, lineterminator='\n')

    ##filling header information
    for quest in data['questions']:
        data_header.append(quest['question'])
        question_id.append(quest['id'])
        
    data_writer.writerow(data_header)

    ##filling response information
    for response in data['responses']:
        
        data_answers = list()
        
        ##only if form was completed
        if response['completed'] != '0':

            ##check if 
            for i in range(0, len(question_id)):
                if question_id[i] in response['answers']:
                    data_answers.append(response['answers'][question_id[i]])
                else:
                    data_answers.append('NaN')
           
            data_writer.writerow(data_answers)
       
        

##close it down, boys. It is done
write_data.close()




