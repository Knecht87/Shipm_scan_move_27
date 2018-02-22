#import mysql.connector,datetime
import datetime

#Define our data base connectivity and common variables
worker = ''
progee = ''
starter = ''

shipm = 0
zone_from = ''
zone_to = ''

hostname = '192.168.200.10'
username = 'scanner'
password = '%%%%%%%'
database = 'rabendb'
#Checking the date
#now = datetime.datetime.today()

#Function definition for p programm
#def executeSQLp(conn,zone_from,zone_to,login,now,shipm):
#    cursor = conn.cursor()
#    now = datetime.datetime.today()
#    query = "INSERT INTO rabendb.SHIPMENT_MOVE (FROM_ZONE,TO_ZONE,LOGIN,WHENADD,SHIPM)\
#             VALUES ('%s','%s','%s','%s',%s);" % (zone_from,zone_to,login,now,shipm)
#    cursor.execute(query)

worker = raw_input("Enter your scan working number/name: ")

print "Hello, %s, please choose your application:\ni - to start inventarization of leftovers\np - to move shipment to zone"\
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
            else: print "You are ready to scan zone:"
            zone_where = raw_input()
            while zone_where == '' or ' ' in zone_from or zone_from == '0':
                print "zone_from can't be empty/contain spaces, check it and try again"
                zone_where = raw_input()
            else:
                print "You have finished input\nShipment:%s\nWhere: %s" % (shipm,zone_where)
 #               connection = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
 #               executeSQLp(connection,zone_from,zone_to,worker,now,shipm)
 #               connection.close()
 # after several attempts to update python 2.4 on a server to python 2.7 to import mysqlconnector
 # as and implementation flash decision comes to comment the connector and operate with local .csv file
 # so after all variables are set we add line to the .csv file
 # hope to correct it with DB SQL later on
                now = datetime.datetime.today()
                variable_set_string = "%s; %s; %s; %s;\n" % (shipm,zone_where,worker,now)
                file = open('i_progee_scan_file','a')
                file.write(variable_set_string)
                file.close()
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
 #               connection = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
 #               executeSQLp(connection,zone_from,zone_to,worker,now,shipm)
 #               connection.close()
 # after several attempts to update python 2.4 on a server to python 2.7 to import mysqlconnector
 # as and implementation flash decision comes to comment the connector and operate with local .csv file
 # so after all variables are set we add line to the .csv file
 # hope to correct it with DB SQL later on
                now = datetime.datetime.today()
                variable_set_string = "%s; %s; %s; %s; %s;\n" % (shipm,zone_from,zone_to,worker,now)
                file = open('p_progee_scan_file','a')
                file.write(variable_set_string)
                file.close()
            print "Another scan?\nk - go on\nq - quit"
            starter = raw_input()
            while starter != 'k' and starter!= 'q':
                print "Only k or q are available, try again"
                starter = raw_input()
    else:
        break