from string import ascii_lowercase
import requests
import json
import hashlib

# Fazendo requisição HTTP e transformando json em dicionario
site = "https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=2164c8f5a19b4c8a2ebf4db96e716e0afa965c1d"
r = requests.get(site)
dic_request = json.loads(r.text)

# Recuperando informações do dicionario
senha = dic_request["cifrado"]
num_casas = -dic_request["numero_casas"]

# Desencriptando e encriptando
alphabet = ascii_lowercase
criptografia = lambda letra, num : alphabet[alphabet.find(letra) + num]
resultado = ''.join([criptografia(i, num_casas) if i in alphabet else i for i in senha])
encrypt_sha1 = hashlib.sha1(resultado.encode()).hexdigest()

# Atualizando dicionario
dic_request["resumo_criptografico"] = encrypt_sha1
dic_request["decifrado"] = resultado

# Criando arquivo e salvando em json
with open('answer.json', 'w') as outfile:
    json.dump(dic_request, outfile)

# Enviando submissão
url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=2164c8f5a19b4c8a2ebf4db96e716e0afa965c1d"
files = {'answer': ('answer.json', open('answer.json', 'rb'))}
r = requests.post(url, files=files)

# Resultado da submissão
resultado_request = json.loads(r.text)["score"]
print("Sua pontuação foi de %s%%" %resultado_request)
