from tasks import add
from time import sleep

res = add.delay(100,100)
sleep(1)
print('res.ready(): ', res.ready())
print('res.result: ', res.result)