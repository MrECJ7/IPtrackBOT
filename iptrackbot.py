#Name        :IPtrackbot
#Writer(s)   :MrECJ7
#Description :IPTrackbot is Advance IP Tracker tool  useing python
import os
import urllib2
import json
import colorama
colorama.init(autoreset=True)

os.system("clear");
print colorama.Fore.CYAN + """

'####:'########::'########:'########:::::'###:::::'######::'##:::'##:'########:::'#######::'########:
. ##:: ##.... ##:... ##..:: ##.... ##:::'## ##:::'##... ##: ##::'##:: ##.... ##:'##.... ##:... ##..::
: ##:: ##:::: ##:::: ##:::: ##:::: ##::'##:. ##:: ##:::..:: ##:'##::: ##:::: ##: ##:::: ##:::: ##::::
: ##:: ########::::: ##:::: ########::'##:::. ##: ##::::::: #####:::: ########:: ##:::: ##:::: ##::::
: ##:: ##.....:::::: ##:::: ##.. ##::: #########: ##::::::: ##. ##::: ##.... ##: ##:::: ##:::: ##::::
: ##:: ##::::::::::: ##:::: ##::. ##:: ##.... ##: ##::: ##: ##:. ##:: ##:::: ##: ##:::: ##:::: ##::::
'####: ##::::::::::: ##:::: ##:::. ##: ##:::: ##:. ######:: ##::. ##: ########::. #######::::: ##::::
....::..::::::::::::..:::::..:::::..::..:::::..:::......:::..::::..::........::::.......::::::..:::::
                                                                                                     

"""
print"\033[1;33m==================================================================================================\033[1;33m"
print   
print	"\033[1;32mAuthor	      :Mr.ECJ7\033[1;32m"
print	"\033[1;32mGithub	      :https://github.com/MrECJ7\033[1;32m"
print   "\033[1;32mVersion       :1.0V\033[1;32m"
print
print"\033[1;33m==================================================================================================\033[1;33m"

print ("\033[1;32mWelcome to IPtrackBOT\033[1;32m\n")

while True:
 ip = raw_input("What  is your IP:")
 url= "http://ip-api.com/json/"

 response = urllib2.urlopen(url + ip)

 data = response.read()

 value = json.loads(data)

 print('')
 print('')
 print(" IP          : " + value['query'])
 print(" status      : " + value['status'])
 print(" country     : " + value['country'])
 print(" countryCode : " + value['countryCode'])
 print(" region      : " + value['region'])
 print(" regionName  : " + value['regionName'])
 print(" city        : " + value['city'])
 print(" zip         : " + value['zip'])
 print(" org         : " + value['org'])
 print(" isp         : " + value['isp'])
 print(" timezone    : " + value['timezone'])
 print(" as          : " + value['as']) 
 print('')
 print('')
 break

else:
 print('hello')
 
