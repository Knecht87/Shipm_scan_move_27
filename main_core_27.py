#import mysql.connector,datetime
import datetime
import cx_Oracle

#Define our data base connectivity and common variables
worker = ''
progee = ''
starter = ''

shipm = 0
zone_from = ''
zone_to = ''
zone_where = ''
id_val = ''
now = datetime.datetime.today()

connection = cx_Oracle.connect('username/pwd@host/db')
print connection.version + " conneted to KL6"

#Function definition for programm
def executeSQL(conn,shipm,zone_from,zone_to,zone_where,worker,now,id_val):
    cursor = conn.cursor()
    now = datetime.datetime.today()
    shipm = int(shipm)
    zone_from = str(zone_from)
    zone_to = str(zone_to)
    zone_where = str(zone_where)
    worker = str(worker)
    id_val = str(id_val)
    rows = [(shipm,zone_from,zone_to,zone_where,worker,now,id_val)]
    cursor.setinputsizes(int,100,100,100,100,100,100)
    cursor.executemany("INSERT INTO vitaliy.INV_MOVE_TABLE (DOSVLG,FR_ZONE,TO_ZONE,IN_ZONE,WERKNM,SC_DATE,ID_VAL)\
                        VALUES (:1,:2,:3,:4,:5,:6,:7)",rows)
    conn.commit()
    cursor.close()

worker = raw_input("Enter your scan working number/name: ")

print "Hello, %s, choose your application:\ni - to start inventarization of leftovers\np - to move shipment to zone"\
    "\nq - quit" % (worker)
progee = raw_input()
while progee != 'i' and progee != 'p' and progee != 'q':
    print "Only i, p or q are available, try again:"
    progee = raw_input()

#Inventarization of leftovers
while progee == 'i':
    print "Welcome, %s, to inventarization application\nk - to start scan\nq - to quit application" % (worker)
    starter = raw_input ()
    while starter != 'k' and starter != 'q':
        print "Only k or q are available, try again:"
        starter = ''
        starter = raw_input()
    print "Scan zone:"
    zone_where = raw_input()
    while zone_where == '' or ' ' in zone_from or zone_from == '0':
        print "zone_from can't be empty/contain spaces,\ncheck it and try again"
        zone_where = raw_input()
    while starter == 'k':
        print "Scan shipment:"
        shipm = raw_input()
        try:
            shipm = int(shipm)
        except ValueError:
            print "You should've scan shipment!"
        else:
            while shipm < 804000000000000:
                print "Incorrect shipment value try again:"
                shipm = raw_input()
                shipm = int(shipm)
            else:
                print "You have finished input\nShipment:%s\nWhere: %s" % (shipm,zone_where)
                executeSQL(connection,shipm,zone_from,zone_to,zone_where,worker,now,id_val)
            print "Another scan?\nk - go on\nq - quit"
            starter = raw_input()
            while starter != 'k' and starter!= 'q':
                print "Only k or q are available, try again"
                starter = raw_input()
    else:
        break
#Move shipment from zone to zone
while progee == 'p':
    print "Welcome, %s, to shipment flow application\nk - to start scan\nq - to quit application" % (worker)
    starter = raw_input ()
    while starter != 'k' and starter != 'q':
        print "Only k or q are available, try again:"
        starter = ''
        starter = raw_input()
    while starter == 'k':
        print "First scan shipment:"
        shipm = raw_input()
        try:
            shipm = int(shipm)
        except ValueError:
            print "You should've scan shipment!"
        else:
            while shipm < 804000000000000:
                print "Incorrect shipment value try again:"
                shipm = raw_input()
                shipm = int(shipm)
            else: print "You are ready to scan zone_from:"
            zone_from = raw_input()
            while zone_from == '' or ' ' in zone_from or zone_from == '0':
                print "zone_from can't be empty/contain spaces, check it and try again"
                zone_from = raw_input()
            else: print "You are ready to scan zone_to:"
            zone_to = raw_input()
            while zone_to == '' or ' ' in zone_to or zone_to == '0':
                print "zone_to can't be empty/contain spaces, check it and try again:"
                zone_to = raw_input()
            else:
                print "You have finished input\nShipment:%s\nMoving: %s -> %s" % (shipm,zone_from,zone_to)
                executeSQL(connection,shipm,zone_from,zone_to,zone_where,worker,now,id_val)
            print "Another scan?\nk - go on\nq - quit"
            starter = raw_input()
            while starter != 'k' and starter!= 'q':
                print "Only k or q are available, try again"
                starter = raw_input()
    else:
        break

print "We are done here"
connection.close()
