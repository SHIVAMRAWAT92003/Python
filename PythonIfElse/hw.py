import time 
timestamp=time.strftime('%H:%M:%S')
print(timestamp)
hourtimestamp=int(time.strftime('%H'))
print(hourtimestamp)
mintimestamp=int(time.strftime('%M'))
print(mintimestamp)
sectimestamp=int(time.strftime('%S'))
print(sectimestamp)


if(hourtimestamp>=0 and hourtimestamp<12):
    print("GM baby....")

elif(hourtimestamp>12 and hourtimestamp<12):
    print("GA baby....")
else:
    print("GN baby")