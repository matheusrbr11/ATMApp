import time

class Conta():
    def __init__(self,cliente,agencia,numeroConta,saldo):
        self.cliente = cliente
        self.agencia = agencia
        self.numeroConta = numeroConta
        self.saldo = saldo

    def sacar(self, valor):
        if(self.saldo < valor):
            print("Valor insuficiente em conta")
        else:
            self.saldo -= valor
            print("\nSaque realizado de R${:.2f}!".format(valor),"\n--- Saldo: R${:.2f}".format(self.saldo))

    def depositar(self,valor):
        if(valor <= 0):
            print("Não é possivel depositar esse valor!")
        else:
            self.saldo += valor
            print("\nDepósito realizado de R${:.2f}!".format(valor),"\n--- Saldo: R${:.2f}".format(self.saldo))

class Cliente():
    def __init__(self,nome,cpf):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return ("Nome: "+self.nome+"\nCPF: "+self.cpf)

while True:

    nome = str(input("Nome do Titular: "))
    cpf = str(input("CPF do Titular: "))
    agencia = str(input("Digite a Agência: "))
    numero = str(input("Digite o Numero da Conta: "))
    saldo = 0.0

    pessoa1 = Cliente(nome,cpf)
    conta1 = Conta(pessoa1,agencia,numero,saldo)
    
    if agencia == '0001' and numero == '4144':

        print("====================\n"+str(pessoa1),"\n"+"N°Agência:",conta1.agencia,"\n"+"N°Conta:",conta1.numeroConta,"\n"+"Saldo: R${:.2f}".format(conta1.saldo),"\n====================")

        resposta = ''
        lista_resposta = ['1','2','3','X','x']

        while (resposta != 'X' and resposta !='x'):
            resposta = input("[1] PARA CONSULTAR SALDO - [2] PARA DEPÓSITO - [3] PARA SAQUE - [X] PARA SAIR: ")
            if(resposta == '1'):
                print("\n--- SEU SALDO É DE R${:.2f}".format(conta1.saldo))

            elif(resposta == '2'):
                valor = float(input("\nDIGITE O VALOR DO DEPOSITO: "))
                conta1.depositar(valor)

            elif(resposta == '3'):
                valor = float(input("\nDIGITE O VALOR DO SAQUE: "))
                conta1.sacar(valor)
            
            elif(resposta == 'x' or resposta == 'X'):
                exit()

            elif(resposta not in lista_resposta):
                print("\nTENTE NOVAMENTE. . .")

    else:
        print("Agência ou Conta inválida.")
        time.sleep(1)
        print("Tente Novamente")
        time.sleep(1)
        