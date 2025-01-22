import time

start = time.time ()
result = "".join([str(i) for  i in range (1, 10001)])
print ("+= Time:" , time.time () - start)