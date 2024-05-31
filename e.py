from easygui import *
from urllib.request import urlopen
fail = open("luuletus.txt", encoding = "UTF-8")
f = open("andmed.txt", "w")
f2 = open("luuletus.txt", encoding = "UTF-8")
failveebis = urlopen("https://kodu.ut.ee/~marinai/eprogalused/mesipuu.txt")
baidid = failveebis.read()
tekst = baidid.decode()
failveebis.close()
nupud = ["järgmine luuletus"]
vajutus = buttonbox(tekst, choices = nupud)
if vajutus == "järgmine luuletus":
    loetud = fail.readlines()
    formateeritud = ""
    i = 0
    while i < len(loetud):
        formateeritud += loetud[i]
        i += 1
    fail.close()
    nupud2 = ["järgmine küsimus"]
    vajutus = buttonbox(formateeritud, choices = nupud2)
if vajutus == "järgmine küsimus":
    nupud3 = ["luuletus 1", "luuletus 2", "mitte kumbki"]
    vajutus = buttonbox("milline luuletus rohkem meeldis", choices = nupud3)
if vajutus == "luuletus 2":
    nupud4 = ["ok"]
    f.write("luuletus 2 meeldis" + "\n")
    f.close()
if vajutus == "luuletus 1":
    nupud5 = ["ok"]
    f.write("luuletus 1 meeldis" + "\n")
    f.close()
if vajutus == "mitte kumbki":
    loetud2 = f2.readlines()
    formateeritud2 = ""
    i = 0
    while i < len(loetud):
        formateeritud2 += loetud[i]
        i += 1
    f2.close()
    nupud6 = ["meeldis", "ei meeldinud"]
    vajutus = buttonbox(formateeritud2, choices = nupud6)
if vajutus == "ei meeldinud":
    nupud7 = ["ok"]
    vajutus = buttonbox("oeh", choices = nupud7)
if vajutus == "meeldis":
    nupud8 = ["ok"]
    f.write("luuletus 3 meeldis" + "\n")
    f.close()