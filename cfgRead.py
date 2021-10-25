from configparser import ConfigParser 

configur = ConfigParser() 
print (configur.read('/home/pi/Documents/IGY/config.ini')) 

print ("Sections : ", configur.sections())
print ("init : ", configur.get('init','device_uuid')) 
#print ("Log Errors debugged ? : ", configur.getboolean('debug','log_errors')) 
#print ("Port Server : ", configur.getint('server','port')) 
#print ("Worker Server : ", configur.getint('server','nworkers')) 
