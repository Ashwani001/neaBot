#!/usr/bin/env python
from xml.etree import ElementTree as ET
import requests
import pygame, sys
from lxml import etree
from time import sleep
import base64

data_sets=["2hr_nowcast"
,"24hrs_forecast"
,"4days_outlook"#Daily (Rest are hourly)
,"heavy_rain_warning"
,"uvi"
,"earthquake"
,"psi_update"
,"pm2.5_update"]


code=[
['BR','Mist'],
['CL','Cloudy'],
['DR','Drizzle'],
['FA','Fair (Day)'],
['FG','Fog'],
['FN','Fair (Night)'],
['FW','Fair & Warm'],
['HG','Heavy Thundery Showers with Gusty Winds'],
['HR','Heavy Rain'],
['HS','Heavy Showers'],
['HT','Heavy Thundery Showers'],
['HZ','Hazy'],
['LH','Slightly Hazy'],
['LR','Light Rain'],
['LS','Light Showers'],
['OC','Overcast'],
['PC','Partly Cloudy (Day)'],
['PN','Partly Cloudy (Night)'],
['PS','Passing Showers'],
['RA','Moderate Rain'],
['SH','Showers'],
['SK','Strong Winds, Showers'],
['SN','Snow'],
['SR','Strong Winds, Rain'],
['SS','Snow Showers'],
['SU','Sunny'],
['SW','Strong Winds'],
['TL','Thundery Showers'],
['WC','Windy, Cloudy'],
['WD','Windy'],
['WF','Windy, Fair'],
['WR','Windy, Rain'],
['WS','Windy, Shower']]
#add 2hr, psi, humidity, temp, heavy rain

#Used for debuging
def pretty_print(xml_str):
    root = etree.fromstring(xml_str)
    print etree.tostring(root, pretty_print=True)

def url_join(data):
	base_url="http://api.nea.gov.sg/api/WebAPI/?dataset="
	keyref=""#Enter your NEA key here
	data_set_url=data_sets[data]
	url = base_url + data_set_url + "&keyref=" + keyref;
	r = requests.get(url)
	root = ET.fromstring(r.content)
	#pretty_print(r.content)#Used for debugging
	return root

def sound(audio_file):
	pygame.mixer.init()
	#TODO pass song as arg or package one with script
	pygame.mixer.music.load(audio_file)
	pygame.mixer.music.play()
	#pygame.mixer.music.stop()
	while pygame.mixer.music.get_busy() == True:
		continue
	pygame.mixer.music.stop()


def psi_check():
	root=url_join(6)
	for child in root.findall("./item/"):
	        #print child.tag,child.text
		if( child.find('id').text=="rNO"):
        	    for childx in child.find('record'):
	                #print childx.attrib.get('type'),childx.attrib.get('value')
                	if ( childx.attrib.get('type') )=='NO2_1HR_MAX':
        	            if( int(childx.attrib.get('value'))>5):#low value used for demo
				sound("../sounds/psi_high.wav")
				#sound("../sounds/Rain_2hr_MAndarin.wav")
				
def twoHr_check(area):
	root=url_join(0)
	for child in root.findall("./item/weatherForecast/"):
	        if( child.attrib.get('name') == area ):
        	        forecast=child.attrib.get('forecast')
                	for c in code:
				if c[0]==forecast:
					return c[1]
			#if(child.attrib.get('forecast'))=='PN':#This is for heavy rain. i think... 
			#sound("../sounds/rain_alert.wav")


def save_img(img_str,img_name):
	image_64_decode = base64.decodestring(img_str)
	image_result = open(img_name, 'wb')
	image_result.write(image_64_decode)

	
def heavyRain_check():
	root=url_join(3)
	for child in root.findall("./rain_area_image/"):
		imgstring=child.text	
	save_img(imgstring,"rain_area_image.gif") 
	#for child in root.findall("./satellite_image/"):
	#	imgstring=child.text	
	#save_img(imgstring,"satellite_image.png")

#heavyRain_check()#Useless	
#twoHr_check("Geylang")
#psi_check() 



