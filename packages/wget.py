import urequests

def main(argv):
 r = urequests.get(argv[0])
 return r.content.decode('UTF-8')


