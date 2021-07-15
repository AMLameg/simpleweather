from tkinter.constants import TRUE
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import T
import xml_handler as xh
from datetime import datetime
import request

request.conn()

def name(num) -> list:
    
    this_list = []
    keys = []

    newdict = dict((v[0],k) for k,v in xh.tag_lookup_dict.items())

    for foo,bar in xh.data_dict.items():
        if foo == list(xh.data_dict.keys())[num]:
            keys = list(bar.keys())
            break

    for key in keys:
        this_list.append(newdict[key])
            
    return this_list

def data(num) -> list:
    a_list = []

    for k,v in xh.data_dict.items():
        if list(xh.data_dict.keys())[num] in k:
            for key,vals in v.items():
                a_list.append(vals)
    return a_list

def unit(num) -> list:

    unit_list = []
    vals = []

    newdict = dict((v[0],v[1]) for k,v in xh.tag_lookup_dict.items())
    for foo,bar in xh.data_dict.items():
        if foo == list(xh.data_dict.keys())[num]:
            vals = list(bar.keys())
            break

    for val in vals:
        unit_list.append(newdict[val])
    
    return unit_list

def datatodisplay(num) -> str:
    return_str = ''
    i,j = 0,0
    units = unit(num)
    somedata = data(num)

    for elem in name(num) :
        return_str += elem+': '+somedata[j]+' '+units[i]+'\n'
        i+=1
        j+=1
    
    #return_str = ''.join('%s : %s %s \n'%(name(num),data(num),unit(num)))
    return return_str

sg.theme('LightBlue')


tab1_layout = [
    [sg.T(datatodisplay(0))],
]
tab2_layout = [
    [sg.T(datatodisplay(1))],
]
tab3_layout = [
    [sg.T(datatodisplay(2))],
]
tab4_layout = [
    [sg.T(datatodisplay(3))],
]
tab5_layout = [
    [sg.T(datatodisplay(4))],
]
tab6_layout = [
    [sg.T(datatodisplay(5))],
]
tab7_layout = [
    [sg.T(datatodisplay(6))],
]
tab8_layout = [
    [sg.T(datatodisplay(7))],
]
tab9_layout = [
    [sg.T(datatodisplay(8))],
]
tab10_layout = [
    [sg.T(datatodisplay(9))],
]

##todo: loop it idiot

layout = [[sg.Text(xh.city_name,font=('Helvetica',18) )],

           [sg.Text('Data exported at : %s'%(xh.data_requested_date))],

           [sg.Text('Current Time: %s'%(datetime.now().time()))],

           [sg.TabGroup([[sg.Tab('Date: %s'%(list(xh.data_dict.keys())[0]),tab1_layout),

           sg.Tab('Date: %s'%(list(xh.data_dict.keys())[1]),tab2_layout),

           sg.Tab('Date: %s'%(list(xh.data_dict.keys())[2]),tab3_layout),

           sg.Tab('Date: %s'%(list(xh.data_dict.keys())[3]),tab4_layout),

           sg.Tab('Date: %s'%(list(xh.data_dict.keys())[4]),tab5_layout),

           sg.Tab('Date: %s'%(list(xh.data_dict.keys())[5]),tab6_layout),

           sg.Tab('Date: %s'%(list(xh.data_dict.keys())[6]),tab7_layout),

           sg.Tab('Date: %s'%(list(xh.data_dict.keys())[7]),tab8_layout),

           sg.Tab('Date: %s'%(list(xh.data_dict.keys())[8]),tab9_layout),

           sg.Tab('Date: %s'%(list(xh.data_dict.keys())[9]),tab10_layout),]])],

           [sg.Exit()]]

window = sg.Window('Five day Report',layout)

while True:
    event,values = window.read()
    if event in (sg.WIN_CLOSED,'Exit'):
        break

window.close()