from configparser import ConfigParser
from definitions import ROOT
import os

file = os.path.join(ROOT, 'resource', 'config.ini')
config = ConfigParser()
config.read(file)

path = config['PATH']
host = path['localhost']
port = path['port']
