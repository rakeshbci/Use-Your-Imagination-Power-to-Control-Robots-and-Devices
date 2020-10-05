from osc4py3.as_eventloop import *
from osc4py3 import oscmethod as osm
import time

osc_startup()

def prediction(left, right):
  print(“Left prediction : “,round(left,2),”Right prediction : “,round(right,2))
 
osc_udp_server(“127.0.0.1”, 9002, “neuropype”)
osc_method(“/neuropype”, prediction)
finished = False

while not finished:
  osc_process()
  osc_terminate()
