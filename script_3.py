#!/usr/bin/env python

import json

with open('./disks.json') as json_data:
    dischi=json.load(json_data)

ordinati=sorted(dischi,key=lambda d:d['code'] ,reverse=False)

fout=open('./funzionanti.txt','w')
for disk in ordinati:
    if(disk['working']=='YES'):
        fout.write(disk['code']+'\n')

fout.close()
