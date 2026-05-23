import sys    
import hashlib
import base64 

# hash final que queremos encontrar (resultado do sha1)
hash_alvo = sys.argv[1]

# caminho da wordlist passada por argumento
wordlist = sys.argv[2]

# abre o arquivo da wordlist
with open(wordlist) as f:
    
    # percorre cada linha (cada possível senha)
    for linha in f:
        
        # remove espaços e principalmente o \n do final da linha
        linha = linha.strip()

        # 1º passo: gera o MD5 da senha (em formato hexadecimal)
        md5 = hashlib.md5(linha.encode()).hexdigest()

        # 2º passo: transforma o MD5 (string) em bytes e aplica Base64
        b64 = base64.b64encode(md5.encode())

        # 3º passo: aplica SHA1 no resultado do Base64 e converte para hexadecimal
        sha1 = hashlib.sha1(b64).hexdigest()

        # compara o hash gerado com o hash alvo
        if sha1 == hash_alvo:
            
            # se bater, imprime a senha encontrada
            print(linha)
            break
