#!/usr/bin/env python

import datetime
import sys
import calendar

dtin=sys.argv[1]
giorno, mese, anno = (int(x) for x in dtin.split('/'))  
datain=datetime.date(anno,mese,giorno)
giorno_sett=calendar.day_name[datain.weekday()]
print(giorno_sett)

today=datetime.datetime.now().date()
delta=(today-datain).days
print(delta)

