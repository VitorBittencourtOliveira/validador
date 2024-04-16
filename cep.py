import requests

class Busca_endereco:
    def __init__ (self, cep):
        cep = str(cep)

        if self.cep_e_validado(cep):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!")

    def __str__(self):
        return self.cep_formatado()

    def cep_e_validado(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def cep_formatado(self):
        return "{}-{}".format(self.cep[:5],self.cep[5:])
    
    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (dados["logradouro"], dados["bairro"], dados["localidade"], dados["uf"])