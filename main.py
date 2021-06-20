import json
import re
import csv
json = json.loads(open('input.json').read())

my_list = []

for i in json['items']:
    try:
        # this is obviously hideos but I don't have time to tidy right now
        text_dict = i['text']
        text = str(text_dict.values())
        text = text.replace('\n\t',' ')
        text = text.replace('\n',' ')
        text = text.replace('\\n',' ')
        text = text.replace('\\t','')
        text = text.replace('dict_values([','')
        text = text.replace('])','')
        text = text.replace('"','')
        text = text.rstrip()
        text = text.replace("'","")
        re.sub(r"(?<=[a-z])\r?\n"," ", text)
        my_list.append(text)
    except:
        pass

file=open('output.txt','w')
for items in my_list:
    file.writelines(items+'\n')
file.close()