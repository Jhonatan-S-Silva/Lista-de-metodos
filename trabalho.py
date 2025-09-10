#Crie uma classe Aluno com os atributos nome e notas (lista de notas). 
#Crie um método que calcule a média das notas do aluno. 
#Crie um método que verifique se o aluno foi aprovado (média ≥ 7). 
#Sugestão de teste: criando pelo menos dois objetos. 

class Aluno:
    def __init__(self,nome, notas):
        self.nome = nome
        self.notas = notas
    
    def calcular_media(self):
        if len(self.notas) == 0:
            return 0
        return sum(self.notas) / len(self.notas)
    
    def aprovados(self):
        return self.calcular_media () >= 7
    
    #teste com 2 alunos

aluno1 = Aluno("Maria", [8, 7, 9])
aluno2 = Aluno("macarrão",[5, 3, 5])

print("\n__________________exercicio 12____________________________")

print(f"Aluno: {aluno1.nome}")
print(f"Notas: {aluno1.notas}")
print(f"Média: {aluno1.calcular_media():.2f}")
print("Aprovado" if aluno1.aprovados() else "Reprovado")
print()

print(f"Aluno: {aluno2.nome}")
print(f"NOtas:{aluno2.notas}")
print(f"media: {aluno2.calcular_media():.2f}")
print("aprovado" if aluno2.aprovados() else "Reprovado")


#Crie uma classe Produto com nome e preço. 
#Implemente o método __str__ para exibir o produto. 
#Implemente o método __eq__ para comparar dois produtos pelo preço. 
#Sugestão de teste: comparar dois objetos. 

class produto:
    def __init__(self,nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Produto: {self.nome}, Preço: R${self.preco:.2f}"
    
    def __eq__(self, outro):
        if isinstance(outro, produto):
            return  self.preco == outro.preco
        return False
    
p1 = produto("Notebook", 3500.00)
p2 = produto("Celular", 3500.00)
p3 = produto("Fone de ouvido", 200.00)
print("\n__________________exercicio 12____________________________")
print(p1) 
print(p2)

#Crie uma classe Mensagem com um método enviar que possa receber apenas texto (str) 
#ou números inteiros (int) e um destinatário específico. 
#Sugestão de teste: testar com as duas formas de uso.

class Mensagem:
    def __init__(self, receptor):
        self.receptor = receptor
    
    def enviar(self, pacote):
        if isinstance(pacote, (str,int)):
             print(f"Enviando '{pacote}' para {self.receptor}")
        else:
            raise TypeError("a mensagem só pode ser (str) ou (int) se não for um dos dois não pide poha, mescreve essa bagaça certa")

print("\n__________________exercicio 15____________________________")
m1 = Mensagem("João")
m1.enviar("eaeww seu noóia?")
m1.enviar(1345)             

        





