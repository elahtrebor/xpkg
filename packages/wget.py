import urequests

def exec(url):
 r = urequests.get(url)
 return r.content.decode('UTF-8')

