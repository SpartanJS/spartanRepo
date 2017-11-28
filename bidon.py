from time import sleep
from time import time
from random import randint
from IPython.display import clear_output

start_time = time()
requests = 0

for _ in range(1):
    # A request would go here
    requests += 1
    sleep(randint(1,1))
    current_time = time()
    elapsed_time = current_time - start_time
    print('Request: {}; Frequency: {} requests/s'.format(requests, requests/elapsed_time))
    clear_output(wait : bool)

for i in range(10):
    clear_output(True)
    print("Hello World!")

print ('hello')
