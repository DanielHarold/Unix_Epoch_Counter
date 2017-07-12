import time

#Press CTRL C to interrupt the unix_countup function:
def unix_countup(party=1500000000):
    '''Unix Time Stamp Counter.
    
    unix_countup(party)
    party:= counter end time.
    
    Example:
    unix_countup(party=1600000000)
    '''
    
    while True:
        if time.time()<party:
            print("{:,}".format(time.time()))
            wait_time = 1-time.time()%1
            time.sleep(wait_time if wait_time else 1)
        else:
            break
    
    print('1.5 Billion!')



#add parameter option: asc|desc time.
