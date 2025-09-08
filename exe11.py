class Matematica:
    @staticmethod
    def eh_primo(numero):
        if numero < 2:
            return False
        for i in range(2, int(numero**0.5) + 1):
            if numero % i == 0:
                return False
        return True


print(Matematica.eh_primo(2))   
print(Matematica.eh_primo(4))   
print(Matematica.eh_primo(17))  
print(Matematica.eh_primo(20))  
