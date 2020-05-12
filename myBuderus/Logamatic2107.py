from datetime import datetime

#	"hk1_betriebsart" => "070065656565%02x65:0702%02x",
# 	my %km271_set_betriebsart = ("nacht"     => 0,"tag"       => 1,"automatik" => 2,);
#	<li>hk1_betriebsart [automatik|nacht|tag]<br>
#         sets the working mode for heating circuit 1<br>
#          <ul>
#            <li>automatik: the timer program is active and the summer configuration is in effect</li>
#            <li>nacht: manual by night working mode, no timer program is in effect</li>
#            <li>tag: manual by day working mode, no timer program is in effect</li>
#          </ul></li>




#	"CFG_Sommer_ab"                 => "0000:1,p:-9,a:8",
#	"CFG_HK1_Nachttemperatur"       => "0000:2,d:2",
#	"cFG_HK1_Nachttemperatur"       => "0700:0,d:2",  # fake reading for internal notify
#	"CFG_HK1_Tagtemperatur"         => "0000:3,d:2",
#	"cFG_HK1_Tagtemperatur"         => "0701:0,d:2",  # fake reading for internal notify

#	"CFG_HK1_Betriebsart"           => "0000:4,a:4",
#	"cFG_HK1_Betriebsart"           => "0702:0,a:4",  # fake reading for internal notify

#	"CFG_HK1_Max_Temperatur" 	=> "000e:2",
#	"CFG_HK1_Auslegung" 		=> "000e:4",
#	"CFG_HK1_Aufschalttemperatur" 	=> "0015:0,a:9",
#	"CFG_Frost_ab" 			=> "0015:2,s",

#	"CFG_HK1_Absenkungsart"         => "001c:1,a:6",
#	"CFG_HK1_Heizsystem"            => "001c:2,a:7",


#	"CFG_HK1_Temperatur_Offset" 	=> "0031:3,s,d:2",
#    	"CFG_HK1_Fernbedienung"     	=> "0031:4,a:0",
#    	"CFG_Frost_ab"              	=> "0031:5,s",
#    	"cFG_Frost_ab"            	=> "0707:0,s",  # fake reading for internal notify
#    	"CFG_HK2_Nachttemperatur" 	=> "0038:2,d:2",
#    	"cFG_HK2_Nachttemperatur" 	=> "0802:0,d:2",  # fake reading for internal notify
#    	"CFG_HK2_Tagtemperatur" 	=> "0038:3,d:2",
#	"cFG_HK2_Tagtemperatur" 	=> "0803:0,d:2",  # fake reading for internal notify
#	"CFG_HK2_Betriebsart"   	=> "0038:4,a:4",
#	"cFG_HK2_Betriebsart"   	=> "0804:0,a:4",  # fake reading for internal notify
#	"CFG_HK2_Urlaubtemperatur" 	=> "0038:5,d:2",
#	"cFG_HK2_Urlaubtemperatur" 	=> "0805:0,d:2",  # fake reading for internal notify

#	"CFG_HK2_Max_Temperatur"      	=> "0046:2",
#	"CFG_HK2_Auslegung"           	=> "0046:4",
#	"CFG_HK2_Aufschalttemperatur" 	=> "004d:0,a:9",
#	"CFG_WW_Vorrang"              	=> "004d:1,a:0",
#	"CFG_HK2_Aussenhalt_ab"       	=> "004d:2,s",
#	"cFG_HK2_Aussenhalt_ab" 	=> "0806:0,s",    # fake reading for internal notify

#	"CFG_HK2_Absenkungsart" 	=> "0054:1,a:6",
#	"CFG_HK2_Heizsystem"    	=> "0054:2,a:7",
#	"CFG_HK2_Temperatur_Offset" 	=> "0069:3,s,d:2",
#	"CFG_HK2_Fernbedienung"     	=> "0069:4,a:0",
#	"CFG_Gebaeudeart"           	=> "0070:2,a:13",
#	"CFG_WW_Temperatur"         	=> "007e:3",
#	"cFG_WW_Temperatur"   		=> "0c07:0",        # fake reading for internal notify
#	"CFG_WW_Betriebsart" 	 	=> "0085:0,a:4",
#	"cFG_WW_Betriebsart"  		=> "0c0e:0,a:4",    # fake reading for internal notify
#	"CFG_WW_Aufbereitung" 		=> "0085:3,a:0",
#	"CFG_WW_Zirkulation"  		=> "0085:5,a:11",
#	"cFG_WW_Zirkulation"  		=> "0c0f:0,a:11",   # fake reading for internal notify
#	"CFG_Sprache"         		=> "0093:0,a:3",
#	"CFG_Anzeige"         		=> "0093:1,a:1",
#	"CFG_Brennerart"              	=> "009a:1,p:-1,a:12",
#	"CFG_Max_Kesseltemperatur"    	=> "009a:3",
#	"CFG_Pumplogik"               	=> "00a1:0",
#	"CFG_Abgastemperaturschwelle" 	=> "00a1:5,p:-9,a:5",
#	"CFG_Brenner_Min_Modulation"  	=> "00a8:0",
#	"CFG_Brenner_Mod_Laufzeit"    	=> "00a8:1",



#	"PRG_HK1_Programm" 		=> "0100:0,a:2",
#	"CFG_Urlaubstage" 		=> "0100:3",
#	"PRG_HK1_Timer01" 		=> "0107:0,t",
#	"PRG_HK1_Timer02" 		=> "010e:0,t",
#	"PRG_HK1_Timer03" 		=> "0115:0,t",
#	"PRG_HK1_Timer04" 		=> "011c:0,t",

#	"PRG_HK1_Timer14"    		=> "0162:0,t",

#	"PRG_HK2_Programm"   		=> "0169:0,a:2",
#	"PRG_HK2_Timer01"    		=> "0170:0,t",
#	"PRG_HK2_Timer02"    		=> "0177:0,t",

#	"PRG_HK2_Timer14"   		=> "01cb:0,t",
#	"CFG_Uhrzeit_Offset" 		=> "01e0:1,s",


#	"ERR_Fehlerspeicher1"           => "0300:0,eh",
#	"ERR_Fehlerspeicher2"           => "0307:0,eh",
#	"ERR_Fehlerspeicher3"           => "030e:0,eh",
#	"ERR_Fehlerspeicher4"           => "0315:0,eh",

#	"HK1_Betriebswerte1"            => "8000:0,bf:0",
#	"HK1_Betriebswerte2"            => "8001:0,bf:1",
#	"HK1_Vorlaufsolltemperatur"     => "8002:0",
#	"HK1_Vorlaufisttemperatur" 	=> "8003:0,ne", 	# great part of all messages
#	"HK1_Raumsolltemperatur" 	=> "8004:0,d:2",
#	"HK1_Raumisttemperatur" 	=> "8005:0,d:2",
#	"HK1_Einschaltoptimierung" 	=> "8006:0",
#	"HK1_Ausschaltoptimierung" 	=> "8007:0",
#	"HK1_Pumpe" 			=> "8008:0",
#	"HK1_Mischerstellung" 		=> "8009:0,ne", 	# great part of all messages
#	"HK1_Heizkennlinie_+10_Grad" 	=> "800c:0",
#	"HK1_Heizkennlinie_0_Grad" 	=> "800d:0",
#	"HK1_Heizkennlinie_‐10_Grad" 	=> "800e:0",
#	"HK2_Betriebswerte1" 		=> "8112:0,bf:0",
#	"HK2_Betriebswerte2" 		=> "8113:0,bf:1",
#	"HK2_Vorlaufsolltemperatur" 	=> "8114:0",
#	"HK2_Vorlaufisttemperatur" 	=> "8115:0,ne", # great part of all messages
#	"HK2_Raumsolltemperatur" 	=> "8116:0,d:2",
#	"HK2_Raumisttemperatur" 	=> "8117:0,d:2",
#	"HK2_Einschaltoptimierung" 	=> "8118:0",
#	"HK2_Ausschaltoptimierung" 	=> "8119:0",
#	"HK2_Pumpe" 			=> "811a:0",
# 	"HK2_Mischerstellung" 		=> "811b:0,ne",
#	"Nicht_belegt" 			=> "811c:0",
#	"Nicht_belegt" 			=> "811d:0",
#	"HK2_Heizkennlinie_+10_Grad" 	=> "811e:0",
#	"HK2_Heizkennlinie_0_Grad" 	=> "811f:0",
#	"HK2_Heizkennlinie_‐10_Grad" 	=> "8120:0",
#	"Nicht_belegt" 			=> "8121:0",
#	"Nicht_belegt" 			=> "8122:0",
#	"Nicht_belegt" 			=> "8123:0",
#	"WW_Betriebswerte1" 		=> "8424:0,bf:2",
#	"WW_Betriebswerte2" 		=> "8425:0,bf:3",
#	"WW_Solltemperatur" 		=> "8426:0",
#	"WW_Isttemperatur" 		=> "8427:0",
#	"WW_Einschaltoptimierung" 	=> "8428:0",
#	"WW_Pumpentyp" 			=> "8429:0,bf:5",
#	"Kessel_Vorlaufsolltemperatur" 	=> "882a:0",
#	"Kessel_Vorlaufisttemperatur" 	=> "882b:0,ne", 	# great part of all messages
#	"Brenner_Einschalttemperatur" 	=> "882c:0",
#	"Brenner_Ausschalttemperatur" 	=> "882d:0",
#	"Kessel_Integral1" 		=> "882e:0,ne",
#	"Kessel_Integral" 		=> "882f:0,mb:2,ne", 	# great part of all messages
#	"Kessel_Fehler" 		=> "8830:0,bf:6",
#	"Kessel_Betrieb" 		=> "8831:0,bf:4",
#	"Brenner_Ansteuerung" 		=> "8832:0,a:10",
#	"Abgastemperatur" 		=> "8833:0",
#	"Brenner_Mod_Stellglied" 	=> "8834:0",
#	"Nicht_belegt" 			=> "8835:0",
#	"Brenner_Laufzeit1_Minuten2" 	=> "8836:0",
#	"Brenner_Laufzeit1_Minuten1" 	=> "8837:0",
#	"Brenner_Laufzeit1_Minuten" 	=> "8838:0,mb:3",
#	"Brenner_Laufzeit2_Minuten2" 	=> "8839:0",
#	"Brenner_Laufzeit2_Minuten1" 	=> "883a:0",
#	"Brenner_Laufzeit2_Minuten" 	=> "883b:0,mb:3",
#	"Aussentemperatur" 		=> "893c:0,s",
#	"Aussentemperatur_gedaempft" 	=> "893d:0,s",
#	"Versionsnummer_VK" 		=> "893e:0",
#	"Versionsnummer_NK" 		=> "893f:0",
#	"Modulkennung" 			=> "8940:0",
#	"Nicht_belegt" 			=> "8841:0",
#	"ERR_Letzter_Fehlerstatus" 	=> "aa:0,em",
#	"ERR_Alarmstatus" 		=> "aa42:0,bf:7"


def DecodingDay(sDay):
    wynik = ""
    if sDay == "0":
        wynik = "Poniedziałek"
    elif sDay == "2":
        wynik = "Wtorek"
    elif sDay == "4":
        wynik = "Środa"
    elif sDay == "6":
        wynik = "Czwartek"
    elif sDay == "8":
        wynik = "Piątek"
    elif sDay == "A":
        wynik = "Sobota"
    elif sDay == "C":
        wynik = "Niedziela"
    else:
        wynik = "?????"

    return wynik


def DecodingTime(sTime):
    wynik = "test"
    a = int(sTime,16)
    b = int(a / 6)
    c = a % 6

    if b < 10:
        wynik = "0" + str(b) + ":" + str(c) + "0"
    else:
        wynik = str(b) + ":" + str(c) + "0"
    return wynik


def DecodingTimeMessage(sMessage):
    wynik = ""
    if sMessage[2][1] == "0":
        wynik = wynik + "\n" + "NOC   od " + DecodingTime(sMessage[3])
    else:
        wynik = wynik + "\n" + "DZIEŃ od " + DecodingTime(sMessage[3])

    wynik = wynik + "  - " + DecodingDay(sMessage[2][0])

    if sMessage[4][1] == "0":
        wynik = wynik + "\n" + "NOC   od " + DecodingTime(sMessage[5])
    else:
        wynik = wynik + "\n" + "DZIEŃ od " + DecodingTime(sMessage[5])

    wynik = wynik + "  - " + DecodingDay(sMessage[4][0])

    if sMessage[6][1] == "0":
        wynik = wynik + "\n" + "NOC   od " + DecodingTime(sMessage[7])
    else:
        wynik = wynik + "\n" + "DZIEŃ od " + DecodingTime(sMessage[7])

    wynik = wynik + "  - " + DecodingDay(sMessage[6][0])

    #DecodingMessage = DecodingMessage + "\n" + message[2] + " - " + message[2][0] + " - " + message[2][1]
    #DecodingMessage = DecodingMessage + "\n" + message[4] + " - " + message[4][0] + " - " + message[4][1]
    #DecodingMessage = DecodingMessage + "\n" + message[6] + " - " + message[6][0] + " - " + message[6][1]

    return wynik



T_AusTemp = " 0"
T_Ein = " 0"
T_Aus = " 0"
T_Kessel = " 0"
T_Test = " 0"
P_8000 = " 0"
P_8001 = " 0"
P_8002 = " 0"
P_8003 = " 0"
P_8004 = " 0"
P_8008 = " 0"
P_8112 = " 0"
P_8113 = " 0"
P_8114 = " 0"
P_8115 = " 0"
P_8116 = " 0"
P_8424 = " 0"
P_8425 = " 0"
P_8426 = " 1"
P_8427 = " 0"
P_8428 = " 0"
P_8429 = " 0"
P_882A = " 0"
P_8830 = " 0"
P_8831 = " 0"
P_8832 = " 0"
P_8833 = " 0"
P_8834 = " 0"
P_8835 = " 0"
P_8836 = " 0"
P_8837 = " 0"
P_8838 = " 0"
P_8839 = " 0"
P_883A = " 0"
P_883B = " 0"
P_893D = " 0"



def DataGet():
    tab = [10]
    tab[0] = T_AusTemp
    tab[1] = T_Ein
    tab[2] = T_Aus
    tab[3] = T_Kessel
    tab[4] = T_Test

    return tab


def MessageDecoding(message):

    DecodingMessage = ""

    KodRozkazu = message[0] + message[1]
    
    sendMessage = True

    if KodRozkazu == '0000':
        DecodingMessage = "CFG_Sommer_ab = " + str(int(message[3],16)) + " [Sommer=9, Winter=31]"
    elif KodRozkazu[0:1] == 'AA':
        DecodingMessage = "ERR_Letzter_Fehlerstatus = " + str(int(message[1],16)) + " [Error]"
    elif KodRozkazu == '2210':
        DecodingMessage = ""
        sendMessage = False
    
    elif KodRozkazu == '000E':
        DecodingMessage = "CFG_HK1_Max_Temperatur = " + str(int(message[4],16)) + " [°C]\n"
        DecodingMessage = DecodingMessage + "<------ CFG_HK1_Auslegung = " + str(int(message[6],16)) + "[]"

    elif KodRozkazu == '0015':
        DecodingMessage = "CFG_HK1_Aufschalttemperatur = " + str(int(message[2],16)) + " [°C]\n"
        DecodingMessage = DecodingMessage + "<------ CFG_Frost_ab = " + str(int(message[4],16)) + "[°C]"

    elif KodRozkazu == '001C':
        DecodingMessage = "CFG_HK1_Absenkungsart = " + str(int(message[3],16)) + "[Abschalt,Reduziert,Raumhalt,Aussenhalt]\n"
        DecodingMessage = DecodingMessage + "<------ CFG_HK1_Heizsystem = " + str(int(message[4],16)) + "[Aus,Heizkoerper,-,Fussboden]"

    elif KodRozkazu == '0100':
        DecodingMessage = "PRG_HK1_Programm = " + str(int(message[2],16)) + " [Eigen,Familie,Frueh,Spaet,Vormittag,Nachmittag,Mittag,Single,Senior]\n"
        DecodingMessage = DecodingMessage + "<------ CFG_Urlaubstage = " + str(int(message[5],16)) + "[]"
    elif KodRozkazu == '0107':
        DecodingMessage = "PRG_HK1_Timer01 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
        DecodingMessage = DecodingMessage + DecodingTimeMessage(message)
    elif KodRozkazu == '010E':
        DecodingMessage = "PRG_HK1_Timer02 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
        DecodingMessage = DecodingMessage + DecodingTimeMessage(message)
    elif KodRozkazu == '0115':
        DecodingMessage = "PRG_HK1_Timer03 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
        DecodingMessage = DecodingMessage + DecodingTimeMessage(message)
    elif KodRozkazu == '011C':
        DecodingMessage = "PRG_HK1_Timer04 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
        DecodingMessage = DecodingMessage + DecodingTimeMessage(message)
    elif KodRozkazu == '0123':
        DecodingMessage = "PRG_HK1_Timer05 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
        DecodingMessage = DecodingMessage + DecodingTimeMessage(message)
    elif KodRozkazu == '012A':
        DecodingMessage = "PRG_HK1_Timer06 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
        DecodingMessage = DecodingMessage + DecodingTimeMessage(message)
    elif KodRozkazu == '0131':
        DecodingMessage = "PRG_HK1_Timer07 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
        DecodingMessage = DecodingMessage + DecodingTimeMessage(message)
    elif KodRozkazu == '0138':
        DecodingMessage = "PRG_HK1_Timer08 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
        DecodingMessage = DecodingMessage + DecodingTimeMessage(message)
    elif KodRozkazu == '013F':
        DecodingMessage = "PRG_HK1_Timer09 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
        DecodingMessage = DecodingMessage + DecodingTimeMessage(message)
    elif KodRozkazu == '0146':
        DecodingMessage = "PRG_HK1_Timer10 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
        DecodingMessage = DecodingMessage + DecodingTimeMessage(message)
    elif KodRozkazu == '014D':
        DecodingMessage = "PRG_HK1_Timer11 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
        DecodingMessage = DecodingMessage + DecodingTimeMessage(message)
    elif KodRozkazu == '0154':
        DecodingMessage = "PRG_HK1_Timer12 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
        DecodingMessage = DecodingMessage + DecodingTimeMessage(message)
    elif KodRozkazu == '015B':
        DecodingMessage = "PRG_HK1_Timer13 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
        DecodingMessage = DecodingMessage + DecodingTimeMessage(message)
    elif KodRozkazu == '0162':
        DecodingMessage = "PRG_HK1_Timer14 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
        DecodingMessage = DecodingMessage + DecodingTimeMessage(message)
    elif KodRozkazu == '0169':
        DecodingMessage = "PRG_HK2_Programm = " + str(int(message[2],16)) + " [Eigen,Familie,Frueh,Spaet,Vormittag,Nachmittag,Mittag,Single,Senior]\n"
        DecodingMessage = DecodingMessage + "<------ CFG_Urlaubstage = " + str(int(message[5],16)) + "[]"
    elif KodRozkazu == '0170':
        DecodingMessage = "PRG_HK2_Timer01 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
    elif KodRozkazu == '0177':
        DecodingMessage = "PRG_HK2_Timer02 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
    elif KodRozkazu == '017E':
        DecodingMessage = "PRG_HK2_Timer03 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
    elif KodRozkazu == '0185':
        DecodingMessage = "PRG_HK2_Timer04 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
    elif KodRozkazu == '018C':
        DecodingMessage = "PRG_HK2_Timer05 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
    elif KodRozkazu == '0193':
        DecodingMessage = "PRG_HK2_Timer06 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
    elif KodRozkazu == '019A':
        DecodingMessage = "PRG_HK2_Timer07 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
    elif KodRozkazu == '01A1':
        DecodingMessage = "PRG_HK2_Timer08 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
    elif KodRozkazu == '01A8':
        DecodingMessage = "PRG_HK2_Timer09 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
    elif KodRozkazu == '01AF':
        DecodingMessage = "PRG_HK2_Timer10 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
    elif KodRozkazu == '01B6':
        DecodingMessage = "PRG_HK2_Timer11 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
    elif KodRozkazu == '01BD':
        DecodingMessage = "PRG_HK2_Timer12 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
    elif KodRozkazu == '01C4':
        DecodingMessage = "PRG_HK2_Timer13 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"
    elif KodRozkazu == '01CB':
        DecodingMessage = "PRG_HK2_Timer14 = " + str(int(message[2],16)) + str(int(message[3],16)) + str(int(message[4],16)) + str(int(message[5],16)) + str(int(message[6],16)) + str(int(message[7],16)) + " [time]"


    elif KodRozkazu == '01E0':
        DecodingMessage = "CFG_Uhrzeit_Offset = " + str(int(message[3],16)) + " []"


    elif KodRozkazu == '0300':
        DecodingMessage = "ERR_Fehlerspeicher1 = " + str(int(message[2],16)) + " []"
        if (int(message[2],16) == 0) and (int(message[3],16) == 0) and (int(message[4],16) == 0) and (int(message[5],16) == 0) and (int(message[6],16) == 0) and (int(message[7],16) == 0):
            sendMessage = False
    elif KodRozkazu == '0307':
        DecodingMessage = "ERR_Fehlerspeicher2 = " + str(int(message[2],16)) + " []"
    elif KodRozkazu == '030E':
        DecodingMessage = "ERR_Fehlerspeicher3 = " + str(int(message[2],16)) + " []"
    elif KodRozkazu == '0315':
        DecodingMessage = "ERR_Fehlerspeicher4 = " + str(int(message[2],16)) + " []"
    elif KodRozkazu == '8000':
        DecodingMessage = "HK1_Betriebswerte1 = " + str(int(message[2],16)) + " [‐,Ausschaltoptimierung,Einschaltoptimierung,Automatik,Warmwasservorrang,Estrichtrocknung,Ferien,Frostschutz,Manuell]"
        global P_8000
        P_8000 = str(int(message[2],16))
    elif KodRozkazu == '8001':
        DecodingMessage = "HK1_Betriebswerte2 = " + str(int(message[2],16)) + " [‐,Sommer,Tag,Keine Kommunikation mit FB,FB fehlerhaft,Fehler Vorlauffuehler,Maximaler Vorlauf,Externer Stoehreingang,Frei]"
        global P_8001
        P_8001 = str(int(message[2],16))
    elif KodRozkazu == '8002':
        DecodingMessage = "HK1_Vorlaufsolltemperatur = " + str(int(message[2],16)) + " °C"
        global P_8002
        P_8002 = str(int(message[2],16))
    elif KodRozkazu == '8003':
        DecodingMessage = "HK1_Vorlaufisttemperatur = " + str(int(message[2],16)) + " °C"
        global P_8003
        P_8003 = str(int(message[2],16))
    elif KodRozkazu == '8004':
        DecodingMessage = "HK1_Raumsolltemperatur = " + str(int(message[2],16)/2) + " °C"
        global P_8004
        P_8004 = str(int(message[2],16))
    elif KodRozkazu == '8005':
        DecodingMessage = "HK1_Raumisttemperatur = " + str(int(message[2],16)/2) + " °C"
    elif KodRozkazu == '8006':
        DecodingMessage = "HK1_Einschaltoptimierung = " + str(int(message[2],16)) + " °C"
    elif KodRozkazu == '8007':
        DecodingMessage = "HK1_Ausschaltoptimierung = " + str(int(message[2],16)) + " °C"
    elif KodRozkazu == '8008':
        DecodingMessage = "HK1_Pumpe = " + str(int(message[2],16)) + " [0-100%]"
        global P_8008
        P_8008 = str(int(message[2],16))
    elif KodRozkazu == '8009':
        DecodingMessage = "HK1_Mischerstellung = " + str(int(message[2],16)) + " [-]"
    elif KodRozkazu == '800C':
        DecodingMessage = "HK1_Heizkennlinie_+10_Grad = " + str(int(message[2],16)) + " [-]"
    elif KodRozkazu == '800D':
        DecodingMessage = "HK1_Heizkennlinie_0_Grad = " + str(int(message[2],16)) + " [-]"
    elif KodRozkazu == '800E':
        DecodingMessage = "HK1_Heizkennlinie_-10_Grad = " + str(int(message[2],16)) + " [-]"
    elif KodRozkazu == '8112':
        DecodingMessage = "HK2_Betriebswerte1 = " + str(int(message[2],16)) + " °C"
        global P_8112
        P_8112 = str(int(message[2],16))
    elif KodRozkazu == '8113':
        DecodingMessage = "HK2_Betriebswerte2 = " + str(int(message[2],16)) + " °C"
        global P_8113
        P_8113 = str(int(message[2],16))
    elif KodRozkazu == '8114':
        DecodingMessage = "HK2_Vorlaufsolltemperatur = " + str(int(message[2],16)) + " °C"
        global P_8114
        P_8114 = str(int(message[2],16))
    elif KodRozkazu == '8115':
        DecodingMessage = "HK2_Vorlaufisttemperatur = " + str(int(message[2],16)) + " °C"
        global P_8115
        P_8115 = str(int(message[2],16))
    elif KodRozkazu == '8116':
        DecodingMessage = "HK2_Raumsolltemperatur = " + str(int(message[2],16)) + " °C"
        global P_8116
        P_8116 = str(int(message[2],16))
    elif KodRozkazu == '8117':
        DecodingMessage = "HK2_Raumisttemperatur = " + str(int(message[2],16)) + " °C"
    elif KodRozkazu == '8118':
        DecodingMessage = "HK2_Einschaltoptimierung = " + str(int(message[2],16)) + " °C"
    elif KodRozkazu == '8119':
        DecodingMessage = "HK2_Ausschaltoptimierung = " + str(int(message[2],16)) + " °C"
    elif KodRozkazu == '811A':
        DecodingMessage = "HK2_Pumpe = " + str(int(message[2],16)) + " [-]"
    elif KodRozkazu == '811B':
        DecodingMessage = "HK2_Mischerstellung = " + str(int(message[2],16)) + " [-]"
    elif KodRozkazu == '811C':
        DecodingMessage = "Nieużywane = " + str(int(message[2],16)) + " [-]"
        sendMessage = True
    elif KodRozkazu == '811D':
        DecodingMessage = "Nieużywane = " + str(int(message[2],16)) + " [-]"
        sendMessage = True
    elif KodRozkazu == '811E':
        DecodingMessage = "HK2_Heizkennlinie_+10_Grad = " + str(int(message[2],16)) + " [-]"
    elif KodRozkazu == '811F':
        DecodingMessage = "HK2_Heizkennlinie_0_Grad = " + str(int(message[2],16)) + " [-]"
    elif KodRozkazu == '8120':
        DecodingMessage = "HK2_Heizkennlinie_-10_Grad = " + str(int(message[2],16)) + " [-]"
    elif KodRozkazu == '8121':
        DecodingMessage = "Nieużywane = " + str(int(message[2],16)) + " [-]"
    elif KodRozkazu == '8122':
        DecodingMessage = "Nieużywane = " + str(int(message[2],16)) + " [-]"
    elif KodRozkazu == '8123':
        DecodingMessage = "Nieużywane = " + str(int(message[2],16)) + " [-]"
    elif KodRozkazu == '8424':
        DecodingMessage = "WW_Betriebswerte1 = " + str(int(message[2],16)) + " [‐,Automatik,Desinfektion,Nachladung,Ferien,Fehler Desinfektion,Fehler Fuehler,Fehler WW bleibt kalt,Fehler Anode]"
    elif KodRozkazu == '8425':
        DecodingMessage = "WW_Betriebswerte2 = " + str(int(message[2],16)) + " [‐,Laden,Manuell,Nachladen,Ausschaltoptimierung,Einschaltoptimierung,Tag,Warm,Vorrang]"
        global P_8425
        P_8425 = str(int(message[2],16))
    elif KodRozkazu == '8426':
        DecodingMessage = "WW_Solltemperatur = " + str(int(message[2],16)) + " °C"
        global P_8426
        P_8426 = str(int(message[2],16))
    elif KodRozkazu == '8427':
        DecodingMessage = "WW_Isttemperatur = " + str(int(message[2],16)) + " °C"
        global P_8427
        P_8427 = str(int(message[2],16))
    elif KodRozkazu == '8428':
        DecodingMessage = "WW_Einschaltoptimierung = " + str(int(message[2],16)) + " []"
    elif KodRozkazu == '8429':
        DecodingMessage = "WW_Pumpentyp = " + str(int(message[2],16)) + " [‐,Ladepumpe,Zirkulationspumpe,Absenkung Solar,Frei,Frei,Frei,Frei,Frei]"
        global P_8429
        P_8429 = str(int(message[2],16))
    elif KodRozkazu == '882A':
        DecodingMessage = "Kessel_Vorlaufsolltemperatur = " + str(int(message[2],16)) + " °C"
        global P_882A
        P_882A = str(int(message[2],16))
    elif KodRozkazu == '882B':
        DecodingMessage = "Kessel_Vorlaufisttemperatur = " + str(int(message[2],16)) + " °C"
        global T_Kessel
        T_Kessel = str(int(message[2],16))
    elif KodRozkazu == '882C':
        DecodingMessage = "Brenner_Einschalttemperatur = " + str(int(message[2],16)) + " °C"
        global T_Ein
        T_Ein = str(int(message[2],16))
    elif KodRozkazu == '882D':
        DecodingMessage = "Brenner_Ausschalttemperatur = " + str(int(message[2],16)) + " °C"
        global T_Aus
        T_Aus = str(int(message[2],16))
    elif KodRozkazu == '882E':
        DecodingMessage = "Kessel_Integral1 = " + str(int(message[2],16)) + " [-]"
        DecodingMessage = "No"
    elif KodRozkazu == '882F':
        DecodingMessage = "Kessel_Integral = " + str(int(message[2],16)) + " [-]"
        DecodingMessage = "No"
    elif KodRozkazu == '8830':
        DecodingMessage = "Kessel_Fehler" + str(int(message[2],16)) + " [‐,Brennerstoerung,Kesselfuehler,Zusatzfuehler,Kessel bleibt kalt,Abgasfuehler,Abgas ueber Grenzwert,Sicherungskette ausgeloest,Externe Stoerung]"
        global P_8830
        P_8830 = str(int(message[2],16))
    elif KodRozkazu == '8831':
        DecodingMessage = "Kessel_Betrieb" + str(int(message[2],16)) + "[-,Abgastest,Betrieb 1.Stufe,Kesselschutz,Unter Betrieb,Leistung frei,Leistung hoch,Betrieb 2.Stufe,Frei]"
        global P_8831
        P_8831 = str(int(message[2],16))
    elif KodRozkazu == '8832':
        DecodingMessage = "Brenner_ansteuerung = " + str(int(message[2],16)) + " [-]"
        global P_8832
        P_8832 = str(int(message[2],16))
    elif KodRozkazu == '8833':
        DecodingMessage = "Abgastemperatur = " + str(int(message[2],16)) + " [-]"
        global P_8833
        P_8833 = str(int(message[2],16))
    elif KodRozkazu == '8834':
        DecodingMessage = "Brenner_Mod_Stellglied = " + str(int(message[2],16)) + " [-]"
        global P_8834
        P_8834 = str(int(message[2],16))
    elif KodRozkazu == '8835':
        DecodingMessage = "Nieużywany = " + str(int(message[2],16)) + " [-]"
        global P_8835
        P_8835 = str(int(message[2],16))
    elif KodRozkazu == '8836':
        DecodingMessage = "Brennerlaufzeit 1 Stunden 2 = " + str(int(message[2],16)) + " [-]"
        global P_8836
        P_8836 = str(int(message[2],16))
    elif KodRozkazu == '8837':
        DecodingMessage = "Brennerlaufzeit 1 Stunden 1 = " + str(int(message[2],16)) + " [-]"
        global P_8837
        P_8837 = str(int(message[2],16))
    elif KodRozkazu == '8838':
        DecodingMessage = "Brennerlaufzeit 1 Stunden 0 = " + str(int(message[2],16)) + " [-]"
        global P_8838
        P_8838 = str(int(message[2],16))
    elif KodRozkazu == '8839':
        DecodingMessage = "Brennerlaufzeit 2 Stunden 2 = " + str(int(message[2],16)) + " [-]"
        global P_8839
        P_8839 = str(int(message[2],16))
    elif KodRozkazu == '883A':
        DecodingMessage = "Brennerlaufzeit 2 Stunden 1 = " + str(int(message[2],16)) + " [-]"
        global P_883A
        P_883A = str(int(message[2],16))
    elif KodRozkazu == '883B':
        DecodingMessage = "Brennerlaufzeit 2 Stunden 0 = " + str(int(message[2],16)) + " [-]"
        global P_883B
        P_883B = str(int(message[2],16))
    elif KodRozkazu == '893C':
        DecodingMessage = "Aussentemperatur = " + str(int(message[2],16)) + " °C"
        global T_AusTemp
        T_AusTemp = str(int(message[2],16))
        sendMessage = False
    elif KodRozkazu == '893D':
        DecodingMessage = "Aussentemperatur_gedaempft = " + str(int(message[2],16)) + " °C"
        global P_893D
        P_893D = str(int(message[2],16))
    elif KodRozkazu == '893E':
        DecodingMessage = "Versionnummer_VK = " + str(int(message[2],16)) + " []"
    elif KodRozkazu == '893F':
        DecodingMessage = "Versionnummer_NK = " + str(int(message[2],16)) + " []"
    elif KodRozkazu == '8940':
        DecodingMessage = "Modulkennung = " + str(int(message[2],16)) + " []"
    elif KodRozkazu == '8941':
        DecodingMessage = "Nieużywany = " + str(int(message[2],16)) + " []"
    elif ((KodRozkazu == '0310') and (len(message) == 2)):
        DecodingMessage = "No"
    else:
        DecodingMessage = "????????????????????_" + KodRozkazu + "_"


    

    if sendMessage and DecodingMessage != "No":
        now=datetime.now()
        fileName = "/home/pi/myHome/myLogs/Buderus_" + now.strftime("%Y%m%d") + ".txt"
        file = open(fileName,"a")
        file.write(now.strftime("%Y.%m.%d %H:%M:%S") + '\n')
        file.write("<------ " + DecodingMessage + '\n')
        file.write("<------ Message ")
        file.write(str(message))
        file.write('\n') 
        file.write('----------------------------------------------------\n')
        file.close()




def DataWrite():
    global T_Test
    now=datetime.now()
    fileName = "/home/pi/myHome/myScripts/Buderus_144.txt"
    file = open(fileName,"w")
    file.write('----------------------------------------------------\n')
    file.write(now.strftime("%Y.%m.%d %H:%M:%S") + '\n')
    file.write('----------------------------------------------------\n')
    file.write('  144 = ' + T_AusTemp + '       \n')		#'$893C - Aussentemperatur
    file.write('  145 = ' + P_8000 + '       \n')		#'$8000 - Betriebswerte 1 HK1
    file.write('  146 = ' + P_8003 + '       \n')		#'$8003 - Vorlaufisttemperatur HK1
    file.write('  147 = ' + P_882A + '       \n')		#'$882A - Kesselvorlaufsolltemperatur
    file.write('  148 = ' + P_8004 + '       \n')		#'$8004 - Raumsolltemperatur HK1
    file.write('  149 = ' + P_8008 + '       \n')		#'$8008 - Pumpenleistung HK1
    file.write('  150 = ' + P_8427 + '       \n')		#'$8427 - Warmwasseristtemperatur
    file.write('  151 = ' + P_8426 + '       \n')		#'$8426 - Warmwassersolltemperatur
    file.write('  152 = ' + P_8429 + '       \n')		#'$8429 - Ladepumpe
    file.write('  153 = ' + P_8425 + '       \n')		#'$8425 - Betriebswerte 2 WW
    file.write('  154 = ' + '11' + '       \n')		#' Licznik załączeń palnika
    file.write('  155 = ' + P_8836 + '       \n')		#'$8836 - Brennerlaufzeit 1 Stunden 2
    file.write('  156 = ' + P_8837 + '       \n')		#'$8837 - Brennerlaufzeit 1 Stunden 1
    file.write('  157 = ' + P_8838 + '       \n')		#'$8838 - Brennerlaufzeit 1 Stunden 0
    file.write('  158 = ' + T_Aus + '         \n')		#'$882c - Brennereinschalttemperatur
    file.write('  159 = ' + T_Ein + '         \n')		#'$882d - Brennerausschalttemperatur
    file.write('----------------------------------------------------\n')
    file.close()

    fileName = "/home/pi/myHome/myScripts/Buderus_160.txt"
    file = open(fileName,"w")
    file.write('----------------------------------------------------\n')
    file.write(now.strftime("%Y.%m.%d %H:%M:%S") + '\n')
    file.write('----------------------------------------------------\n')
    file.write('  160 = ' + P_8424 + '       \n') 		#'$8424 - Betriebswerte 1 WW
    file.write('  161 = ' + P_8428 + '       \n') 		#'$8428 - Warmwasseroptimierungszeit	
    file.write('  162 = ' + P_8832 + '         \n')       	#'$8832 - Brenneransteuerung -  Palnik
    file.write('  163 = ' + T_Kessel + '         \n') 		#'$882B - Kesselvorlaufisttemperatur
    file.write('  164 = ' + '21' + '         \n') 		#'$882e - Kesselintegral 1
    file.write('  165 = ' + '22' + '         \n') 		#'$882e - Kesselintegral 2
    file.write('  166 = ' + '23' + '         \n') 		#'$8830 - Kesselfehler
    file.write('  167 = ' + '24' + '         \n') 		#'$8831 - Kesselbetrieb
    file.write('  168 = ' + '25' + '         \n') 		#'?????
    file.write('  169 = ' + '26' + '         \n')		#'?????
    file.write('  170 = ' + P_893D + '       \n')		#'$893D - Aussentemperatur 'gedaempfte     
    file.write('  171 = ' + P_8001 + '       \n')		#'$8001 - Betriebswerte 2 HK1  
    file.write('  172 = ' + '29' + '         \n')  
    file.write('  173 = ' + '30' + '         \n')  
    file.write('  174 = ' + '31' + '         \n')		#'Rej.R28: Rejestr pomocniczy  
    file.write('  175 = ' + T_Test  + '         \n')
    file.write('----------------------------------------------------\n')  
    file.close()



def DataRead():
    fileName = "/home/pi/myHome/myScripts/Buderus_144.txt"
    file = open(fileName,"r")  
    for sLine in file:
        nr = sLine[2:5]
        if nr == "144":
            global T_AusTemp
            T_AusTemp = sLine[7:15].strip()
        elif nr == "145":
            global P_8000
            P_8000 = sLine[7:15].strip()
        elif nr == "146":
            global P_8003
            P_8003 = sLine[7:15].strip()
        elif nr == "147":
            global P_882A
            P_882A = sLine[7:15].strip()
        elif nr == "148":
            global P_8004
            P_8004 = sLine[7:15].strip()
        elif nr == "149":
            global P_8008
            P_8008 = sLine[7:15].strip()
        elif nr == "150":
            global P_8427
            P_8427 = sLine[7:15].strip()
        elif nr == "151":
            global P_8426
            P_8426 = sLine[7:15].strip()
        elif nr == "152":
            global P_8429
            P_8429 = sLine[7:15].strip()
        elif nr == "153":
            global P_8425
            P_8425 = sLine[7:15].strip()
        elif nr == "154":
            xxxx = sLine[7:15].strip()
        elif nr == "155":
            global P_8836
            P_8836 = sLine[7:15].strip()
        elif nr == "156":
            global P_8837
            P_8837 = sLine[7:15].strip()
        elif nr == "157":
            global P_8838
            P_8838 = sLine[7:15].strip()
        elif nr == "158":
            global T_Aus
            T_Aus = sLine[7:15].strip()
        elif nr == "159":
            global T_Ein
            T_Ein = sLine[7:15].strip()    
        else:
            print (sLine[2:5] + ' = ' + sLine[7:20].strip())
    file.close()

    fileName = "/home/pi/myHome/myScripts/Buderus_160.txt"
    file = open(fileName,"r")
    for sLine in file:
        nr = sLine[2:5]
        if nr == "160":
            global P_8424
            P_8424 = sLine[7:15].strip()
        elif nr == "161":
            global P_8428
            P_8428 = sLine[7:15].strip()
        elif nr == "162":
            global P_8832
            P_8832 = sLine[7:15].strip()
        elif nr == "163":
            global T_Kessel
            T_Kessel = sLine[7:15].strip()
        elif nr == "170":
            global P_893D
            P_893D = sLine[7:15].strip()
        else:
            print (sLine[2:5] + ' = ' + sLine[7:15].strip())  
    file.close()
    
    global T_Test 
    T_Test = "99"


