import os
import time
import requests
import base64

class DDNSClient:
    def __init__(self):
        self._user_name = ""
        self._password = ""
        self._my_domain = ""
        self._get_ip_website = "https://checkip.amazonaws.com"#https://domains.google.com/checkip banned by Chinese GFW
        self.__myip = ""#receive from self._get_ip_website
        self.__base64()

    def _start(self):
        #if your server can't reach domains.google.com, ssr is required
        # os.system("ssr start")
        while True:
            self.__post_ip_address()
            time.sleep(300)

    def __get_host_ip(self):
        _ip = ""
        try:
            _ip = requests.get(self._get_ip_website).text.strip()
        except:
            print("error when requesting ip ")
        return _ip

    def __post_ip_address(self):
        try:
            #if your server can't reach domains.google.com, proxychains is required
            # os.system("proxychains curl -i -H 'Authorization:Basic "+self.__base64()+"' -H 'User-Agent: google-ddns-updater email@yourdomain.com' https://"+self._user_name+":"+self._password+"@domains.google.com/nic/update?hostname="+self._my_domain+" -d 'myip="+self.__get_host_ip()+"' > /dev/null")
            os.system("curl -i -H 'Authorization:Basic "+self.__base64()+"' -H 'User-Agent: google-ddns-updater email@yourdomain.com' https://"+self._user_name+":"+self._password+"@domains.google.com/nic/update?hostname="+self._my_domain+" -d 'myip="+self.__get_host_ip()+"' > /dev/null")
        except:
            print("error when updating ip ")

    def __base64(self):
        theString = self._user_name+":"+self._password
        encoded_string = base64.b64encode(theString.encode('ascii') )
        return encoded_string.decode('ascii')

if __name__ == '__main__':
    ss = DDNSClient()
    ss._start()