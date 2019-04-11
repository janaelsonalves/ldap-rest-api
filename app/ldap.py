
from ldap3 import Server, Connection, ALL

class LDAP:

    __connection = None
    __host = "ldap://ldap1.prdf.mpf.mp.br"
    base = "o=prdf"
    instances = 0

    @staticmethod
    def get_connection():
        if LDAP.__connection == None:
            LDAP.__connection = LDAP.__create_connection()
        return LDAP.__connection

    @staticmethod
    def __create_connection():
        server = Server(LDAP.__host, get_info=ALL)
        conn = Connection(server, auto_bind=True)
        LDAP.instances += 1
        return conn