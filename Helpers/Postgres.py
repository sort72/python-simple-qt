import psycopg2

class Postgres(object):
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Postgres, cls).__new__(cls)
			cls.conn = psycopg2.connect(database="hospitales", user="postgres", password="1234")
			cls.cursor = cls.conn.cursor()
			cls.seed(cls)
		return cls.instance

	def seed(cls):
		# cls.cursor.execute("delete from hospitals")
		# cls.cursor.execute("delete from doctors")
		cls.cursor.execute("select count(*) from hospitals")
		hospitals = cls.cursor.fetchone()
		if not hospitals[0]:
			hospitals = {
				1: {
					"name": "San Jorge",
					"doctors": { "Juan Jose": "Endocrino", "Carlos": "General", "Maria Jose": "Internista", "Vanessa": "Neurologo" }
				},
				2: {
					"name": "Comfamiliar",
					"doctors": {"Pedro": "Internista", "Pablo": "Nutricionista", "Nicolas M": "General", "Pancho": "General", "Alejandro": "Dermatologo"}
				},
				3: {
					"name": "Megacentro",
					"doctors": {"Mariana": "General", "Nicolas": "Endocrino", "Betty": "General", "Armando": "Urologo"}
				},
				4: {
					"name": "Los Rosales",
					"doctors": {"Argemiro": "Pediatra", "Esteban": "General", "Carla": "Endocrino"}
				},
			}
			for key, data in hospitals.items():
				sql = "INSERT INTO hospitals(hospital_id, hospital_name) values(%s, %s)"
				values=(key, data['name'])
				cls.cursor.execute(sql, values)

				for doctor_name, doctor_speciality in data['doctors'].items():
					sql = "INSERT INTO doctors(hospital_id, doctor_name, speciality) values(%s, %s, %s)"
					values=( key, doctor_name, doctor_speciality)
					cls.cursor.execute(sql, values)
			
			cls.conn.commit()
			print(f"Database seeded with {len(hospitals.keys())} hospitals")
			

