from validar_cpf_cnpj import Documento, DocCpf, DocCnpj
from telefones_br import Telefones_br
from datas_br import Datas_br
from cep import Busca_endereco

exemplo_nome = "Vitor Bittencourt Oliveira"
exemplo_cpf = "45882477000"
exemplo_cnpj = "34798295000105"
doc_cpf = Documento.cria_documento(exemplo_cpf)
doc_cnpj = Documento.cria_documento(exemplo_cnpj)
print(doc_cpf)
print(doc_cnpj)

telefone = "5519997958459"
telefone_obj = Telefones_br(telefone)
print(telefone_obj)

cadastro = Datas_br()
print(cadastro)

print(cadastro.tempo_cadastro())

cep = 13279025
obj_cep = Busca_endereco(cep)
print(obj_cep)

logradouro, bairro, cidade, uf = obj_cep.acessa_via_cep()
print(bairro, cidade, uf)
print("--------------------------------------------------")
print("""Usuário: {}
CPF: {}
CNPJ: {}
Telefone: {}
CEP: {}
Logradouro: {}, {}, {} - {}
Tempo de cadastro: {}
      
Data de hoje: {}
{}, {}
""".format(exemplo_nome, doc_cpf, doc_cnpj, telefone_obj, obj_cep, logradouro, bairro, cidade, uf, cadastro.tempo_cadastro(), cadastro.data_formatada(), cadastro.dia_semana(), cadastro.mes_cadastro()))