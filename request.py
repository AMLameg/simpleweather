import requests
import xml_handler as xh
from dotenv import dotenv_values

#pulls data from .env file containing information
cfg = dotenv_values('.env')

areacode = '324221'
requested = 'daily'
urlloc = ('http://datapoint.metoffice.gov.uk/public/data/val/wxfcs/all/xml/%s?res=%s&key=%s'%(areacode,requested,''.join(values for keys,values in cfg.items())))

def conn():
    try:
        r = requests.get(urlloc)
        xh.writefile(r.text) ## returns string data to be sent into an xml file
    except ConnectionError:
        '''Did not connect properly to target server, try again'''
        pass