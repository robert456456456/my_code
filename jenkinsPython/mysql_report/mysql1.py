__author__ = 'qaa'
import MySQLdb
import datetime

test_name1 = "av_update"

def dbconect(db_ip,db_user,db_pw,db_name):
    db = MySQLdb.connect(host=db_ip, user=db_user, passwd=db_pw, db=db_name)
    cur = db.cursor()
    return cur
def db(db_ip,db_user,db_pw,db_name):
    db = MySQLdb.connect(host=db_ip, user=db_user, passwd=db_pw, db=db_name)

    return db
cur1=dbconect("192.168.1.248","anton","12345","qa")
db1=db("192.168.1.248","anton","12345","qa")

db =db1
cur = db.cursor()
test_name = test_name1
bob = []
print test_name
cur.execute("SELECT id FROM test where `Name` = '" + test_name + "' and `Type` = 'Test'")

for row in cur.fetchall():
 tests_id = row[0]
try:
    #sql_rec = "SELECT vm_name, snap_name FROM vm_tests where test_id = " + str(tests_id) + ";"
    sql_rec="SELECT vm_name, snap_name FROM vm_tests where test_id = " + str(tests_id) + " "'ORDER BY vm_tests.vm_name ASC'";"
    cur.execute(sql_rec)
    for row in cur.fetchall():
     #sql_rec1 = "INSERT INTO tasks (vm_name, snap_name, date, time, status, test_id) VALUES ('" + row[0] + "', '" + row[1] + "', '" + str(datetime.date.today()) + "', '" + str(datetime.datetime.now().strftime("%H:%M:%S")) + "', 6, " + str(tests_id) + ");"
     sql_rec1 ="DELETE FROM tasks WHERE test_id = '" + str(tests_id) +"' and vm_name = '" + row[0] + "' and snap_name = '" + row[1] + "' and status = '6';"
     print "send " + sql_rec1
     cur.execute(sql_rec1)
     db.commit()
except MySQLdb.Error, e:
 print "An error has been passed. %s" %e

