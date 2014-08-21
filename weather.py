#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import xml.dom.minidom
from gismeteo.parser import GisMeteoParser, _Forecast
import argparse


class CustomGisMeteoParser(GisMeteoParser):
	def html_for_service(self):
		town = self.first_data
		s = []
		for f in town.forecasts:
			s.append(f._tod)   #0
			s.append(f._date)
			s.append(f._phenom)
			s.append(f._temp) # Температура
			s.append(f._wind) # Ветер
			s.append(f._press) # Давление
			s.append(f._wet) # Влажность
			s.append(f._picture) # Изображение облаков
		return s

def create_parser():
		parser = argparse.ArgumentParser()
		parser.add_argument ('-day', '-d', nargs='?', type=int, default=0)
		parser.add_argument ('status', nargs='?', choices=["datetime", "cloud_cover", "ccloud_cover","pressure", "temperature", "humidity", "wwind_direction", "wind_velocity"])
		return parser

if __name__ == '__main__':
	conkycloud = {
    u'clear':'а',
    u'clarify':'b',
    u'clarify':'c',
    u'cloudy':'d',
    u'rain':'q',
    u'rain':'r',
    u'snow':'t',
    u'snow':'k',
    u'storm':'v',
    u'clear':'E',}
	wind = {
	'с':'9',
	'с-в':';',
	'в':'=',
	'ю-в':'?',
	'ю':'1',
	'ю-з':'?',
	'з':'5',
	'с-з':'7',
	'ШТЛ':'%',}
	gmp = CustomGisMeteoParser(town_id=28642) # для г. Челябинск
	parser = create_parser()
	namespaces = parser.parse_args(sys.argv[1:])
	data = gmp.html_for_service()
# -------------Дата и время дня ------------------------
	if (namespaces.day == 0) and (namespaces.status == 'datetime'):
		date = data[1] + ", " + data[0]
		print date.encode('utf8', 'replace')
	if (namespaces.day == 1) and (namespaces.status == 'datetime'):
		date = data[9] + ", " + data[8]
		print date.encode('utf8', 'replace')
	if (namespaces.day == 2) and (namespaces.status == 'datetime'):
		date = data[17] + ", " + data[16]
		print date.encode('utf8', 'replace')
	if (namespaces.day == 3) and (namespaces.status == 'datetime'):
		date = data[25] + ", " + data[24]
		print date.encode('utf8', 'replace')
# ------------- Изображение облаков ------------------------
	if (namespaces.day == 0) and (namespaces.status == 'ccloud_cover'):
		cloudy = data[7]
		print conkycloud[cloudy]
	if (namespaces.day == 1) and (namespaces.status == 'ccloud_cover'):
		cloudy = data[15]
		print conkycloud[cloudy]
	if (namespaces.day == 2) and (namespaces.status == 'ccloud_cover'):
		cloudy = data[23]
		print conkycloud[cloudy]
	if (namespaces.day == 3) and (namespaces.status == 'ccloud_cover'):
		cloudy = data[31]
		print conkycloud[cloudy]
# ------------- Описание облачности ------------------------
	if (namespaces.day == 0) and (namespaces.status == 'cloud_cover'):
		print data[2].encode('utf8', 'replace')
	if (namespaces.day == 1) and (namespaces.status == 'cloud_cover'):
		print data[10].encode('utf8', 'replace')
	if (namespaces.day == 2) and (namespaces.status == 'cloud_cover'):
		print data[18].encode('utf8', 'replace')
	if (namespaces.day == 3) and (namespaces.status == 'cloud_cover'):
		print data[26].encode('utf8', 'replace')
# ------------- Температура------------------------
	if (namespaces.day == 0) and (namespaces.status == 'temperature'):
		print data[3].encode('utf8', 'replace')
	if (namespaces.day == 1) and (namespaces.status == 'temperature'):
		print data[11].encode('utf8', 'replace')
	if (namespaces.day == 2) and (namespaces.status == 'temperature'):
		print data[19].encode('utf8', 'replace')
	if (namespaces.day == 3) and (namespaces.status == 'temperature'):
		print data[27].encode('utf8', 'replace')
# ------------- Направление Ветера------------------------
	if (namespaces.day == 0) and (namespaces.status == 'wwind_direction'):
		direction = data[4].encode('utf')
		if (direction[2:3] == '-'):
			print wind[direction[0:6].strip()]
		else:
			print wind[direction[0:2]]
	if (namespaces.day == 1) and (namespaces.status == 'wwind_direction'):
		direction = data[12].encode('utf')
		if (direction[2:3] == '-'):
			print wind[direction[0:6].strip()]
		else:
			print wind[direction[0:2]]
	if (namespaces.day == 2) and (namespaces.status == 'wwind_direction'):
		direction = data[20].encode('utf')
		if (direction[2:3] == '-'):
			print wind[direction[0:6].strip()]
		else:
			print wind[direction[0:2]]
	if (namespaces.day == 3) and (namespaces.status == 'wwind_direction'):
		direction = data[28].encode('utf')
		if (direction[2:3] == '-'):
			print wind[direction[0:6].strip()]
		else:
			print wind[direction[0:2]]
# ------------- Сила Ветра------------------------
	if (namespaces.day == 0) and (namespaces.status == 'wind_velocity'):
		direction = data[4].encode('utf')
		if (direction[2:3] == '-'):
			print direction[6:16].strip()
		else:
			print direction[2:12].strip()
	if (namespaces.day == 1) and (namespaces.status == 'wind_velocity'):
		direction = data[12].encode('utf')
		if (direction[2:3] == '-'):
			print direction[6:16].strip()
		else:
			print direction[2:12].strip()
	if (namespaces.day == 2) and (namespaces.status == 'wind_velocity'):
		direction = data[20].encode('utf')
		if (direction[2:3] == '-'):
			print direction[6:16].strip()
		else:
			print direction[2:12].strip()
	if (namespaces.day == 3) and (namespaces.status == 'wind_velocity'):
		direction = data[28].encode('utf')
		if (direction[2:3] == '-'):
			print direction[6:16].strip()
		else:
			print direction[2:12].strip()
# ------------- Давление------------------------
	if (namespaces.day == 0) and (namespaces.status == 'pressure'):
		print data[5].encode('utf8', 'replace')
	if (namespaces.day == 1) and (namespaces.status == 'pressure'):
		print data[13].encode('utf8', 'replace')
	if (namespaces.day == 2) and (namespaces.status == 'pressure'):
		print data[21].encode('utf8', 'replace')
	if (namespaces.day == 3) and (namespaces.status == 'pressure'):
		print data[29].encode('utf8', 'replace')
# ------------- Влажность------------------------
	if (namespaces.day == 0) and (namespaces.status == 'humidity'):
		print data[6].encode('utf8', 'replace')
	if (namespaces.day == 1) and (namespaces.status == 'humidity'):
		print data[14].encode('utf8', 'replace')
	if (namespaces.day == 2) and (namespaces.status == 'humidity'):
		print data[22].encode('utf8', 'replace')
	if (namespaces.day == 3) and (namespaces.status == 'humidity'):
		print data[30].encode('utf8', 'replace')
