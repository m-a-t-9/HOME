from .Logger import *

STATES = {"UNLOCKED": 0, "LOCKED": 1}
AUTH_WAY = {0:"PIN", 1:"FINGERPRINT"}

class DOOR:
  
  __state = None
  __authType = []
  __psw = None
  
  def __init__(self, object):
    self.lg = Logger("syslog.LOG", "DOOR")
    self.__initialize(object)
  
  def __initialize(self, object):
    for child in object:
      if child.tag == "AUTH":
        __authType.append(AUTHORIZATION(child))
  
  def getStates():
    return STATES
    
  def __encrypt(self):
    pass
  
  def __decrypt(self):
    pass