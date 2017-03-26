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

key = "ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d"
uid = "PfSNFM"
data_header = list();
# url = "https://api.typeform.com/v1/form/PfSNFM?key=ac83034cfa742c0f79c26e9a612b4ba7e2aa0d3d"

url = "https://api.typeform.com/v1/form/" + uid + "?key=" + key

resp = requests.get(url)
data = resp.json()





          
if data['http_status'] == 200:
    write_data = open('.\data.csv', 'w', encoding='UTF-8')
    data_writer = csv.writer(write_data)
    
    for quest in data['questions']:
        data_header.append(quest['question'])

    data_writer.writerow(data_header)
##    print(data['responses'][0]['completed'])

    for response in data['responses']:
        data_answers = list()
        if response['completed'] != '0':
            if 'date_46098446' in response['answers']:
                data_answers.append(response['answers']['date_46098446'])
            else:
                data_answers.append('NaN')
            if 'number_46099137' in response['answers']:
                data_answers.append(response['answers']['number_46099137'])
            else:
                data_answers.append('NaN')
            if 'yesno_46099317' in response['answers']:
                data_answers.append(response['answers']['yesno_46099317'])
            else:
                data_answers.append('NaN')
            if 'list_46100308_choice' in response['answers']:
                data_answers.append(response['answers']['list_46100308_choice'])
            else:
                data_answers.append('NaN')
            if 'textarea_46100513' in response['answers']:
                data_answers.append(response['answers']['textarea_46100513'])
            else:
                data_answers.append('NaN')
            data_writer.writerow(data_answers)
        
##        for answer in response['answers']:
##            print(answer)
            
##            if answer['yesno_46099317'] == '' or answer['yesno_46099317'] is None:
##                data_answers.append('NaN')
##            else:
##                data_answers.append(answer['yesno_46099317'])
##        data_writer.writerow(data_answers)

        


write_data.close()






##f = open('E:\document\GitHub\PythonAPI\data.csv', 'w', encoding='UTF-8', newline='')
##f.write(rcomp.text)
##f.close()
