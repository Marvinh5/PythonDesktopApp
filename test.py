__author__ = 'marvin'
print("""
EXEC	@return_value = [dbo].[login]
		@usuario = N'{usuario}',
		@password = N'{password}',
		@MacAddress = N'{mac_address}',
		@Aplicacion = N'{aplicacion}',
		@version = N'{version}'
		""".format(usuario = 'marvin', password='123456', mac_address='61762871800337', aplicacion='Practico', version='1.0'))