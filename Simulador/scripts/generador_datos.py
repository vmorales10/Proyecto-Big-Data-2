#!/usr/bin/python
from subprocess import call
from time import sleep
from ProductsSimulation import ProductsSimulation 
from ContenedorSimulation import ContenedorSimulation 
import os

IOT_AGENT_URL = os.getenv('IOT_AGENT_URL', 'http://localhost:7896/iot/d')
IOT_AGENT_KEY = os.getenv('IOT_AGENT_KEY', '4jggokgpepnvsb2uv4s40d5911')

i=0
while 1==1:
  contenedor = ContenedorSimulation(IOT_AGENT_URL,IOT_AGENT_KEY)
  contenedor.sendData()
  i+=1
 
