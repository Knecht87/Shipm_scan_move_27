import sys,mysql.connector,datetime

#Defibne our data base connectivity and common variables
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

now = datetime.datetime.today()

def executeSQLp(conn,zone_from,zone_to,login,now,shipm):
    cursor = conn.cursor()
    now = datetime.datetime.today()
    query = "INSERT INTO rabendb.SHIPMENT_MOVE (FROM_ZONE,TO_ZONE,LOGIN,WHENADD,SHIPM)\
             VALUES ('%s','%s','%s','%s',%s);" % (zone_from,zone_to,login,now,shipm)
    cursor.execute(query)
#    result = cursor.fetchall()
#    for row in result:
#        print row[0], row[1]


worker = raw_input("Enter your scan working number/name: ")

print "Hello, %s, please choose your application:\ni - to start inventarization of left overs\np - to move shipment to zone"\
    "\nq - quit" % (worker)
progee = raw_input()
while progee != 'i' and progee != 'p' and progee != 'q':
    print "Only i, p or q are available, try again:"
    progee = raw_input()

#Inventarization of leftovers
while progee == 'i':
    print "Welcome, %s, to inventarization application\nk - to start scan\nq - to quit application" % (worker)

#Move shipment from zone to zone
while progee == 'p':
    print "Welcome, %s, to shipment flow application\nk - to start scan\nq - to quit application" % (worker)
    starter = raw_input ()
    while starter != 'k' and starter != 'q':
        print "Only k or q are available, try again:"
        starter = input()
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
                connection = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
                executeSQLp(connection,zone_from,zone_to,worker,now,shipm)
                connection.close()
            print "Another scan?\nk - go on\nq - quit"
            starter = raw_input()
            while starter != 'k' and starter!= 'q':
                print "Only k or q are available, try again"
                starter = raw_input()
    else:
        break


#connection = mysql.connector.connect(host=hostname, user=username, passwd=password, db=database)
#executeSQLp(connection)
#connection.close()