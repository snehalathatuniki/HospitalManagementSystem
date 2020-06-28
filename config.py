import os
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'\xbea\xbc4\x0e\xb5O|]\xaa]S\xcc}\xf5l'
