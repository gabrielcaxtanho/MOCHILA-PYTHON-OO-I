class Conta:


    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor
    def pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = (self.__saldo + self.__limite)
        return valor_a_sacar <= valor_disponivel_a_sacar

    def saca(self, valor):
        if(self.pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} ultrapassa o limite disponivel".format(valor))

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def pagamento(self, valor, destino):
        destino.deposita(valor)
### METODOS GET SAO USADOS PARA RETORNO DE INFORMAÇOES DOS OBEJTOS
    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        print("Chamando o limite")
        return self.__limite

    @limite.setter
    def limite(self, limite):
        print("Modificando o limite")
        self.__limite = limite
  ### Metodos estaticos em OO porem deve sem usado com cuidado no mundo OO POIS METODOS ESTATIVOS AFASTAM O CODIGO DO
#### MUNDO 00 POREM PODEM SER UTEIS PARA A SOLUÇAOO OU INFORMAR ALGO QUE NAO IRA MUDAR
    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco':'237'}