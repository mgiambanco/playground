import psycopg2

class configDB: 
    def connect():
        return psycopg2.connect(
            user= 'postgres',
            host= '127.0.0.1',
            database= 'cheetah',
            password= 'abc123',
            port= '5432'
        )
        

            
