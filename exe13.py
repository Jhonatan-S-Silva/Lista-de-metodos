class Seguranca:
    def __init__(self, mensagem):
        self.mensagem = mensagem

    def _criptografar_mensagem(self):
        return "protegida"

    def exibir_mensagem(self):
        criptografada = self._criptografar_mensagem()
        print(f"Mensagem criptografada: {criptografada}")

s = Seguranca("Dados Confidenciais")
s.exibir_mensagem()
