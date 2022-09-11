import cherrypy
from cherrypy.process import servers
import os
import hashlib
import binascii
import json
import sys

userpass=''

def getFile(filename,mode="r"):
  f = open(filename,mode)
  contents = f.read()
  f.close()
  return contents

def crypt(text, passphrase):
  m = hashlib.md5()
  pad = ""
  last = ""
  text = binascii.hexlify(text)
  while(len(pad) < len(text)):
    encoded = last+passphrase
    m.update(encoded.encode('utf-8'))
    last = m.hexdigest()
    pad = pad + last
  pad = pad[0:len(text)]
  result = ""
  while(len(text) > 0):
    tc = text[0]
    text = text[1:len(text)]
    pc = pad[0]
    pad = pad[1:len(pad)]
    newint = int(str(tc),16) ^ int(str(pc),16)
    newchar = str(hex(newint))[2]
    result = result + newchar
  return binascii.unhexlify(result)

class Commander(object):
  def __init__(self):
    global userpass
    userpass = getFile('passphrase.txt')
    return

  def index(self):
    os.system("C:\\Python27\\apps\\sendkey\\sendspace.exe")
    return getFile('index.html')
  index.exposed = True

if __name__ == '__main__':
    cherrypy.server.socket_host = '0.0.0.0'
    cherrypy.server.socket_port = 8760
    cherrypy.quickstart(Commander())