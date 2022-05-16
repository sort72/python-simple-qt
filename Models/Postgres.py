import psycopg2

class Postgres(object):
	def __new__(cls):
		if not hasattr(cls, 'instance'):
			cls.instance = super(Postgres, cls).__new__(cls)
			cls.conn = psycopg2.connect(database="hospitales", user="postgres", password="1234")
			cls.cursor = cls.conn.cursor()
			cls.migrate(cls)
			cls.seed(cls)
		return cls.instance

	def migrate(cls):
		migrations = (

			"""
			CREATE TABLE IF NOT EXISTS public.hospitals
(
				hospital_id integer NOT NULL,
				hospital_name character varying(100) COLLATE pg_catalog."default",
				CONSTRAINT hospitals_pkey PRIMARY KEY (hospital_id)
			)

			TABLESPACE pg_default;

			ALTER TABLE IF EXISTS public.hospitals
				OWNER to postgres;

			""",

			"""
			CREATE TABLE IF NOT EXISTS public.doctors
			(
				doctor_id integer NOT NULL,
				hospital_id integer NOT NULL,
				doctor_name character varying(100) COLLATE pg_catalog."default",
				speciality character varying(100) COLLATE pg_catalog."default",
				CONSTRAINT doctors_pkey PRIMARY KEY (doctor_id)
			)

			TABLESPACE pg_default;

			ALTER TABLE IF EXISTS public.doctors
				OWNER to postgres;
		
			""",

		)

		for migration in migrations:
			cls.cursor.execute(migration)

		cls.conn.commit()
		print(f"Database migrations executed")

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
			doctor_id = 1
			for key, data in hospitals.items():
				sql = "INSERT INTO hospitals(hospital_id, hospital_name) values(%s, %s)"
				values=(key, data['name'])
				cls.cursor.execute(sql, values)

				for doctor_name, doctor_speciality in data['doctors'].items():
					sql = "INSERT INTO doctors(doctor_id, hospital_id, doctor_name, speciality) values(%s, %s, %s, %s)"
					values=(doctor_id, key, doctor_name, doctor_speciality)
					cls.cursor.execute(sql, values)
					doctor_id += 1
			
			cls.conn.commit()
			print(f"Database seeded with {len(hospitals.keys())} hospitals")
			

