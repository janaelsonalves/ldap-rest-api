from ldap import LDAP

user_attributes = [
  'cn',
  'company',
  'departmentNumber',
  "displayName",
  'dn',
  'employeeNumber',
  'employeeType',
  'facsimileTelephoneNumber',
  'fullName',
  'gidNumber',
  'givenName',
  'groupMembership',
  'homeDirectory',
  'l',
  'lockedByIntruder',
  'loginDisabled',
  'loginGraceLimit',
  'loginGraceRemaining',
  'loginIntruderAddress',
  'loginTime',
  'mail',
  'managerWorkforceID',
  'networkAddress',
  'ou',
  'passwordExpirationInterval' ,
  'passwordExpirationTime',
  'registeredAddress',
  'sn',
  'st',
  'street',
  'telephoneNumber',
  'title',
  'uid',
  'workforceID',
]

class User:

    @staticmethod
    def get_users_by_id(uid):
        conn = LDAP.get_connection()
        # fields = ['st',  'street',  'telephoneNumber',  'title',  'uid',  'workforceID',  'dn']
        # fields = attributesList
        conn.search(LDAP.base, '(&(objectclass=person)(|(uid=*' + uid + '*)(fullName=*' + uid + '*)))', attributes=user_attributes)
        return conn.response_to_json()

    @staticmethod
    def get_users():
        conn = LDAP.get_connection()
        # fields = ['st',  'street',  'telephoneNumber',  'title',  'uid',  'workforceID',  'dn']
        # fields = attributesList
        conn.search(LDAP.base, '(&(objectclass=person)(employeeType>=0))', attributes=user_attributes)
        return conn.response_to_json()

class Group:

    @staticmethod
    def get_groups():
        conn = LDAP.get_connection()
        conn.search(LDAP.base, '(|(objectClass=organizationalUnit)(objectClass=Group))')
        return conn.response_to_json()