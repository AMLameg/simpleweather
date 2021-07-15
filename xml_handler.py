import xml.etree.ElementTree as ET
##gotta love me some spaghetti

## puts the contents of r.text into a processable xml file
filename = 'weather_report.xml'

def writefile(a,b=filename):
    with open(b, 'w') as out:
        out.write(a)
    return None

tree = ET.parse(filename)
root = tree.getroot()

current_date = ''
tags = []
data_dict = {}
dict_list = []
datewithtime = []
tag_lookup_dict = {}
name,units,text_name = [],[],[]

##stinky

for temp in root.findall('Wx'):
    for cats in temp.findall('Param'):
        name.append(cats.get('name'))
        units.append(cats.get('units'))
        text_name.append(cats.text)
    
for i in range(len(temp.findall('Param'))):
    tag_lookup_dict[text_name[i]] = [name[i],units[i]]


## todo: refactor ty
for hold in root.findall('DV'):
    data_requested_date = hold.get('dataDate')

    for locationData in hold.findall('Location'):
        city_name = locationData.get('name')

        for current_data in locationData.findall('Period'):
            current_date=current_data.get('value')
            
            for insight in current_data.findall('Rep'):
                timeofday=insight.text
                occur = set(datewithtime)

                if current_date+timeofday not in occur:
                    occur.add(current_date+timeofday)
                    datewithtime.append(current_date+timeofday)

                for tag in insight.attrib.keys():
                    exists = set(tags)
                
                    if tag not in exists:
                        exists.add(tag)
                        tags.append(tag)

                dict_list.append(insight.attrib)

data_dict = dict(zip(datewithtime,dict_list))