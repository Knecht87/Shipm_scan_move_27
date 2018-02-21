import mysql.connector
print "Welcome to shipment flow application\nk - to start scan\nq - to quit application"
starter = raw_input ()
while starter != 'k' and starter != 'q':
    print "Only k or q are available, try again"
    starter = input()
while starter == 'k':
    print "First scan shipment and then zone_from -> zone_to:"
    shipm = raw_input()
    shipm = int(shipm)
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
    else: print "You have finished input\nShipment:%s\nMoving: %s -> %s" % (shipm,zone_from,zone_to)
    print "Another scan?\nk - go on\nq - quit"
    starter = raw_input()
    while starter != 'k' and starter!= 'q':
        print "Only k or q are available, try again"
        starter = raw_input()


def executeSQL(conn):
    cursor = conn.cursor()
    query = "SELECT * FROM SSCConTrip"
    cursor.execute(query)
    result = cursor.fetchall()
    for row in result:
       print row[0], row[1]

hostname = '192.168.200.10'
username = 'scanner'
password = '%%%%%%%'
database = 'rabendb'

connection = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
executeSQL(connection)
connection.close()