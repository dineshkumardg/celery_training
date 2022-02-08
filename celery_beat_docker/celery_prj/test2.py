from tasks import add
from time import sleep

for i in range(0,100):
    add.delay(100,i)
