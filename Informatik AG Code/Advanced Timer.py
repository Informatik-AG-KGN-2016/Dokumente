import math
import time
print("Das ist ein Timer!(s)econds,(m)inutes,(h)ours,(d)ays")

timeranzeige = int(input("Zahl: "))
timerunit = input("Zeiteinheit: ")

i = timeranzeige
ae = timerunit
alti = i

if ae == "m":
    i *= 60
elif ae == "h":
    i *= 3600
elif ae == "d":
    i *= 86400

def clock_counter(i, ae):
    hourofpower = i
    tdjg = i
    if alti > 60:
        xyz = math.floor(alti/60)
    else:
        xyz = alti
    while i != 0:
        if ae == "s":
            if xyz > 1:
                if  i%60 == 0:
                    print(xyz, i%60, sep=":")
                    time.sleep(1)
                    xyz -= 1
                    i -= 1
                elif i%60 != 0:
                    print(xyz, i%60, sep=":")
                    time.sleep(1)
                    i -= 1
        elif ae == "m":
            if  i%60 == 0:
                print(xyz, i%60, sep=":")
                time.sleep(1)
                xyz -= 1
                i -= 1
            elif i%60 != 0:
                print(xyz, i%60, sep=":")
                time.sleep(1)
                i -= 1
        elif ae == "h":
            if i%60 == 0:
                print(xyz, hourofpower%60, i%60, sep=":")
                time.sleep(1)
                xyz -= 1
                hourofpower -= 1
                i -= 1
            elif i%60 != 0:
                print(xyz, hourofpower%60, i%60, sep=":")
                time.sleep(1)
                i -= 1
        elif ae == "d":
            if i%60 == 0:
                print(xyz, tdjg%24, hourofpower%60, i%60, sep=":")
                time.sleep(1)
                xyz -= 1
                tdjg -= 1
                hourofpower -= 1
                i -= 1
            elif i%60 != 0:
                print(xyz, tdjg%24, hourofpower%60, i%60, sep=":")
                time.sleep(1)
                i -= 1
        if i == 0:
            print("Fertig")

clock_counter(i, ae)
