from threading import Thread
from time import strftime, localtime, sleep
import requests, json, csv, os.path

class parser:
    def __init__(self, ip, password, requests_delay = 20, moving_average_size = 300, data_dir = '', log=True):
        self.details = {"right":"usr","pass":password}
        self.ip = ip
        self.requests_delay = requests_delay
        self.moving_average_size = moving_average_size
        self.data_dir = data_dir
        self.log = log
        self.sid = ''
        self.value = 0
        if log:
            if os.path.isfile(self.data_dir+'main.csv') == False:
                file = open(self.data_dir+'main.csv', 'w')
                file.close()
        self.authenticate()
        loop_thread = Thread(target=self.loop)
        loop_thread.daemon = True
        loop_thread.start()
    def authenticate(self):
        r = requests.post("http://"+self.ip+"/dyn/login.json",  data=json.dumps(self.details))
        s = r.content
        rdetails = json.loads(s)
        self.sid = rdetails["result"]["sid"]
    def loop(self):
        data = {"destDev":[],"keys":["6100_40263F00"]}
        if self.moving_average_size % self.requests_delay != 0:
            raise Exception("moving_average_size modulo requests_delay must be 0!")
        values_size = int(self.moving_average_size / self.requests_delay)
        prevminute = 61
        values = [None]*values_size
        i = 0
        while True:
            if i == values_size:
                i = 0
            url =  "http://"+self.ip+"/dyn/getValues.json?sid="+self.sid
            r = requests.post(url, data=json.dumps(data))
            s = r.content.decode('utf-8')
            if s.find("err") != -1:
                self.authenticate()
            else:
                rdata  = json.loads(s)
                values[i]= rdata["result"]["012F-730A4D39"]["6100_40263F00"]["1"][0]["val"]
                i += 1
                all = 0
                before = 0 
                for x in values:
                    if x == None:
                        all += before
                    else:
                        all += int(x)
                        before = int(x)
                minute = int(strftime("%M", localtime()))
                if minute % 5 == 0 and minute != prevminute and self.log == True:
                    times =  strftime("%H:%M:%S", localtime())
                    date =  strftime("%d.%m.%Y", localtime())
                    day =  strftime("%A", localtime())
                    prevminute =  minute  
                    file = open(self.data_dir+"main.csv", "a")
                    file.write(str(all / len(values)) + ";" + times + ";" + date + ";" + day + ";\n")
                    file.close
                sleep(self.requests_delay)
                self.value = str(int(all / len(values)))