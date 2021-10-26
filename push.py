import requests
import time,sys
time.sleep(5)
res = requests.get(url="http://127.0.0.1:16062/ora_service/getsn")
data=res.json()
res = requests.post(url="http://121.41.205.157:3000/push",data=data)
