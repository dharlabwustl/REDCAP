#!/usr/bin/env python
import requests,json
import pandas as pd
from config import config
import requests, hashlib, json
import os,sys,subprocess
fields = {
    'token': config['api_token'],
    'content': 'record',
    'format': 'json',
    'type': 'flat'
}
r = requests.post('https://redcap.wustl.edu/redcap/api/',data=fields)
r_json=json.dumps(r.json()) #get_niftifiles_metadata(each_axial['URI'] )) get_resourcefiles_metadata(URI,resource_dir)
df_scan = pd.read_json(r_json)
print(df_scan)
df_scan.to_csv('test.csv',index=False)
df_scan=pd.read_csv('test.csv',index_col=False, dtype=object)
############FILTER TO GET THE SINGLE ROW#######################
df_scan_sample=df_scan[(df_scan['redcap_repeat_instance']=="2" ) & (df_scan['record_id']=='ATUL_001')].reset_index()
#######################################################################
field_id='subject_id'
field_value='OURSECONDSUBJECT'
print(df_scan_sample)
record = {
    'redcap_repeat_instrument':str(df_scan_sample.loc[0,'redcap_repeat_instrument']),
    'redcap_repeat_instance':str(df_scan_sample.loc[0,'redcap_repeat_instance']),
    'record_id': str(df_scan_sample.loc[0,'record_id']),
    field_id: field_value

}
data = json.dumps([record])
fields = {
    'token': config['api_token'],
    'content': 'record',
    'format': 'json',
    'type': 'flat',
    'data': data,
}
r = requests.post(config['api_url'],data=fields)
print('HTTP Status: ' + str(r.status_code))
print(r.text)
file = '/home/atul/Downloads/COLI_HM25_CT_1_COLI_HM25_03092021_1954_2_thresh_0_40_VersionDate-11302022_01_07_2023.pdf'
fields = {
    'token': config['api_token'],
    'content': 'file',
    'action': 'import',
    'repeat_instrument':str(df_scan_sample.loc[0,'redcap_repeat_instrument']),
    'repeat_instance':str(df_scan_sample.loc[0,'redcap_repeat_instance']),
    'record': str(df_scan_sample.loc[0,'record_id']),
    'field': 'photo_as_pdf',
    'returnFormat': 'json'
}

file_path=file
file_obj = open(file_path, 'rb')
r = requests.post(config['api_url'],data=fields,files={'file':file_obj})
file_obj.close()

print('HTTP Status: ' + str(r.status_code))
print(r.text)