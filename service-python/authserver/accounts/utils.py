STATUS = (
	(1, 'Active'),
	(2, 'Archive'),
	(3, 'Draft'),
)

def get_status_color(obj):
	warna = ""
	if obj.status == 2:
		warna = 'warning'
	elif obj.status == 3:
		warna = 'info'
	return warna

JENIS_KELAMIN = (
	('Pria', 'Pria'),
	('Wanita', 'Wanita')
)
