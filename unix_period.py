import time
import math

#Press CTRL C to interrupt the unix_countup function:
def unix_countup(offset=0.0):
    '''Unix Time Stamp Counter.
    
    unix_countup(party)
    party:= counter end time.
    
    Example:
    unix_countup(party=1600000000)
    '''
    
    while True:
        print("{:,.0f}".format(math.ceil(time.time() - 0.1)))
        wait_time = 1-(time.time()+offset)%1
        time.sleep(wait_time if wait_time else 1)



#add parameter option: asc|desc time.
