import mysql.connector as sqltor

# NULL in field value is returned as None


try:
	mycon = sqltor.connect(host="localhost", user="saumya", passwd="2020", database="project")

except Exception as e:
	print(e)

else:
	print("Connected to the database")
	curs=mycon.cursor()

	with open("Institutes_Added_to_Check_via_Program (copy)", "r") as fi:
		for s in fi.readlines():
			s = s.split(",")

			name = s[:-1]
			name = ",".join(name)

			if s[-1][-1] == '\n':
				hpg = s[-1][:-1]
			else:
				hpg = s[-1]

			query = 'INSERT INTO records (name, home_page) values(\"'+name+'\",\"'+hpg+'\")'

			try:
				curs.execute(query)
				mycon.commit()
			except Exception as e:
				print(e)
				print(name, hpg)

			# print(name, hpg)

	print("All records added to the database")
	curs.close()
	mycon.close()

