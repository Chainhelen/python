import requests
r = requests.get('http://web1.ouc.edu.cn/_control/validateimage?tt=Wed%20Oct%2022%2013:37:40%20CST%202014')
print r.headers
