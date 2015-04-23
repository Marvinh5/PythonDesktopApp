__author__ = 'marvin'
import pypyodbc as DatabaseConnection
import Config

class Database(object):
    cursor = None
    connection = None

    def connect(self):
        try:
            connection_string =  Config.connectionString()

            self.connection = DatabaseConnection.connect(connection_string)

            self.cursor = self.connection.cursor()

            return self

        except ValueError:
            self.error = ValueError
            return self

    def executeQuery(self, query):
        """:return the headers, the rows in array and the length of the array"""
        try:
            self.cursor.execute(query)

            headers = []
            if(self.cursor.description != None):
                for header in self.cursor.description:
                    headers.append(header)

            rows = []

            current_row = self.cursor.fetchone()

            while current_row != None:
                row = []
                for field in current_row:
                    row.append(field)
                rows.append(row)
                current_row = self.cursor.fetchone()

            return headers, rows, len(rows)
        except ValueError:
            self.cursor.fetchall()
            header[0] = 'IdMensaje'
            header[1] = 'Mensaje'
            row[0][1] = 'Error:'+str(ValueError)
            row[0][0] = 0
            return headers, rows, len(rows)