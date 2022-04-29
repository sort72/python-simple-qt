import Models.Persistence

def main():
	persistence = Models.Persistence.Persistence()
	print(persistence.get_by_id(1))
	print(persistence.get_by_id(3))
	print(persistence.get_by_name('Rosales'))
	print(persistence.get_by_name('San Jorge'))

main()