import os,requests
from PIL import Image

for i in range(0,1):
	f = open(str(i),'wb')
	f.write(requests.get('http://web1.ouc.edu.cn/_control/validateimage?tt=Wed%20Oct%2022%2013:37:40%20CST%202014').content)
im = Image.open('C:\Users\zhaoyong\Desktop\z.jpg')
im.show()
