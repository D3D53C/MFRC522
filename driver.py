
"""driver.py:	RFID class"""

__author__ = "Marc Steinebrunner"
__copyright__ = ""
__version__ = "Development v0.01"
__email__ = "info@time-track.eu"
__status__ = "Dev"


class MFRC522:

def __init__(self):
	self.reader = SimpleMFRC522()

def reader(self):
	try:
        	return  reader.read()
	except Exception as e:
                return e
        finally:
        	GPIO.cleanup()
def writer(self, data):
	try:
        	self.reader.write(data)
		return 200
	except Exception as e:
		return e
	finally:
        	GPIO.cleanup()

