# coding: utf-8

# builtin
import argparse

# local
from hvacir import HVAC_CMD


def main():
    parser = argparse.ArgumentParser(description='Short sample python HVAC_IR command sender to Broadlink RM2 Mini ')
    parser.add_argument('-t', '--temperature', action='store', dest='HVAC_TEMPERATURE', default=21, type=int,
                        help='Set HVAC Temperature in Celcius, Ex: 21')
    parser.add_argument('-p','--power', action='store_true', default=False,
                        dest='HVAC_POWER',
                        help='HVAC Power, default = Power Off')
    parser.add_argument('-c', '--climate', action='store', dest='HVAC_CLIMATE_CODE', default='C',
                        help='Define Climate Code : C=Cold*, H=HOT')
    parser.add_argument('-Vv', '--vanne_vertical', action='store', dest='HVAC_VANNE_V_CODE', default='A',
                        help='Define Vertical Vanne Mode : A=Automatic*, S=Swing, B=Bottom, T:Top')                
    parser.add_argument('-F', '--fan', action='store', dest='HVAC_FAN_MODE', default='A',
                        help='Define Fan speed : A=Automatic*, L=Low, M=Middle, F=Fast, S=Silent')                
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    results = parser.parse_args()
            
    MyHVAC_cmd = HVAC_CMD()    # create an HVAC Command Object
    
    # Parse the Arg Parameters, if any
    # Parse Power On/Off
    if (results.HVAC_POWER):
        MyHVAC_cmd.Power = MyHVAC_cmd.HVAC_Power.On
    else:
        MyHVAC_cmd.Power = MyHVAC_cmd.HVAC_Power.Off
    
    # Parse HVAC Clim Mode    
    if (results.HVAC_CLIMATE_CODE[0:1] == 'C'):
        MyHVAC_cmd.Mode = MyHVAC_cmd.HVAC_Mode.Cold
    elif (results.HVAC_CLIMATE_CODE[0:1] == 'H'):
        MyHVAC_cmd.Mode = MyHVAC_cmd.HVAC_Mode.Hot
    elif (results.HVAC_CLIMATE_CODE[0:1] == 'D'):
        MyHVAC_cmd.Mode = MyHVAC_cmd.HVAC_Mode.Dry
    else:
        MyHVAC_cmd.Mode = MyHVAC_cmd.HVAC_Mode.Auto
    
    # Parse HVAC Fan Mode
    if (results.HVAC_FAN_MODE[0:1] == 'S'):
        MyHVAC_cmd.Fan = MyHVAC_cmd.HVAC_Fan.Silent
    elif (results.HVAC_FAN_MODE[0:1] == '1'):
        MyHVAC_cmd.Fan = MyHVAC_cmd.HVAC_Fan.Speed1
    elif (results.HVAC_FAN_MODE[0:1] == '2'):
        MyHVAC_cmd.Fan = MyHVAC_cmd.HVAC_Fan.Speed2
    elif (results.HVAC_FAN_MODE[0:1] == '3'):
        MyHVAC_cmd.Fan = MyHVAC_cmd.HVAC_Fan.Speed3
    elif (results.HVAC_FAN_MODE[0:1] == '4'):
        MyHVAC_cmd.Fan = MyHVAC_cmd.HVAC_Fan.Speed4
    elif (results.HVAC_FAN_MODE[0:1] == '5'):
        MyHVAC_cmd.Fan = MyHVAC_cmd.HVAC_Fan.Speed5
    else:
        MyHVAC_cmd.Fan = MyHVAC_cmd.HVAC_Fan.Auto
    
    # Parse HVAC_Vanne    Mode / HVAC_VANNE_V_CODE
    if (results.HVAC_FAN_MODE[0:1] == 'S'):
        MyHVAC_cmd.Vanne = MyHVAC_cmd.HVAC_Vanne.Swing
    elif (results.HVAC_FAN_MODE[0:2] == 'B'):
        MyHVAC_cmd.Vanne = MyHVAC_cmd.HVAC_Vanne.H5
    elif (results.HVAC_FAN_MODE[0:1] == 'T'):
        MyHVAC_cmd.Vanne = MyHVAC_cmd.HVAC_Vanne.H1
    else:
        MyHVAC_cmd.Vanne = MyHVAC_cmd.HVAC_Vanne.Auto
    
    # Parse Temperature
    MyHVAC_cmd.Temp = results.HVAC_TEMPERATURE
    
    # display the Cmd built
    print(MyHVAC_cmd.broadlink_cmd_b64())
    #MyHVAC_cmd.broadlink_send_cmd(to_host="192.168.2.96", to_mac="34 ea 34 8a 35 ee")


if __name__ == '__main__':
    main()
