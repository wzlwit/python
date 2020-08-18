# more convenient that urllib
r=requests.get('url',auth=('user','pass'))
r.status_code
r.headers['content-type']
r.encoding
r.text
r.json()