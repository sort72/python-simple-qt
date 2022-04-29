import Models.Postgres as Postgres
import Models.ICrud as ICrud

class Persistence(ICrud.ICrud):

	def __init__(self):
		self.conn = Postgres.Postgres()

	def get_by_id(self, id):
		self.conn.cursor.execute("select * from doctors where doctor_id = %s", [id])
		return self.conn.cursor.fetchone()

	def get_by_name(self, name):
		self.conn.cursor.execute("select * from hospitals where hospital_name LIKE %s", [ '%{}%'.format(name) ] )
		return self.conn.cursor.fetchall()