from codigo.bytebank import Funcionario

#lucas =  Funcionario('Lucas Carvalho', '13/03/2000', 1000)
#print(lucas.idade())

def testaIdade():
    funcionario_teste = Funcionario('teste', '13/03/2000', 1111)
    print(f'teste = {funcionario_teste.idade()}')

testaIdade()