# @staticmethod (Métodos estáticos) s"ao inuteis em Python =)
# Métodos estáticos sao métodos que estão dentro da classe,
# mas n"ao tem acesso ao self nem ao cls.
# Em resumo, sao fun"oes que existem dentro da sua classe.


class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
    
    def set_user(self, user):
        self.user = user
    
    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print('Log: ', msg)


c1 =  Connection.create_with_auth('Lucas', "testes")
print(Connection.log('Mensagem de log'))
# c1 =  Connection()
# c1.set_user('Lucas')
# c1.set_password('Teste')
print(c1.user)
print(c1.password)