 import time

hourvar = int(input("Stunden: "))
minutevar = int(input("Minuten: "))
secondvar = int(input("Sekunden " ))
timelist = [str(hourvar%24), str(minutevar%60), str(secondvar%60)]
alt_hourvar = hourvar
alt_minutevar = minutevar
alt_secondvar = secondvar
while True:
    if hourvar == 0:
        hourvar += 1
        hourvar -= 1
    elif minutevar == 0:
        minutevar += 1
        minutevar -= 1
    elif secondvar == 0:
        break
    print(":".join(timelist))
    secondvar -= 1
    if secondvar%60 == 0:
        minutevar -= 1
    elif minutevar%60 == 0:
        hourvar -= 1
    if hourvar < 10:
        timelist = ["0"+str(hourvar%24), str(minutevar%60), str(secondvar%60)]
    else:
        timelist = [str(hourvar%24), str(minutevar%60), str(secondvar%60)]
    time.sleep(1)
