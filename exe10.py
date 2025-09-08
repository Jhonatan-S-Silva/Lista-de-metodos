class Funcionario:
    empresa = "Sadia"  

    def __init__(self, nome):
        self.nome = nome

    @classmethod
    def alterar_empresa(cls, novo_nome):
        cls.empresa = novo_nome

    def mostrar_dados(self):
        print(f"Nome: {self.nome} | Empresa: {self.empresa}")


f1 = Funcionario("Ana")
f2 = Funcionario("Bruno")

f1.mostrar_dados()  
f2.mostrar_dados()  

Funcionario.alterar_empresa("Perdigão")

f1.mostrar_dados()  
f2.mostrar_dados()  
