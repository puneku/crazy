import mysql.connector as msc

mydb = msc.connect(host="localhost",user="puneku",passwd="pun6sa3rA",database="world")

cursor = mydb.cursor()

cursor.execute("select * from country")

# fetch or save data from cursor

result = cursor.fetchone()  # cursor.fetchall()

for i in result:
	print(i)
