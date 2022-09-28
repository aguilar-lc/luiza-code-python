import jwt
from fastapi import FastAPI, Depends, status, HTTPException, Request

app = FastAPI()

chave_publica = b'''
-----BEGIN PUBLIC KEY-----
MIIBITANBgkqhkiG9w0BAQEFAAOCAQ4AMIIBCQKCAQB+cR/gvgA8JPXoObLf8I37
iDXhsxpRKdC/J4T+PrG9saCPyA8Y6gf4ngdMztPBLWCH1WsxICP3eZPg2zj+Mk+T
oPbSAkgsS12OgjKnNzVP8dVEqtt2d4IbRyyXulFwLEeZVnD1B77P159CgV9fEpEm
QjPMnNinINyvhOHWIlif8GZC6AnmIOB1RbQ59g08xjYrdvM/GHuoqXJCs+8oQs+7
9fYZnQUfLFQe9sNhocjXVKWf2zFJZMNl+VHCyXFRhvhekRKG8Hp4TjIgCnVLefzw
lR7udAH4h4LhWOW3j1WauwSF0Wt1CwbB5o3B3FRS5MmChCw/sfVG/20hk+6ySjoj
AgMBAAE=
-----END PUBLIC KEY-----
'''

chave_privada = b'''
-----BEGIN RSA PRIVATE KEY-----
MIIEoQIBAAKCAQB+cR/gvgA8JPXoObLf8I37iDXhsxpRKdC/J4T+PrG9saCPyA8Y
6gf4ngdMztPBLWCH1WsxICP3eZPg2zj+Mk+ToPbSAkgsS12OgjKnNzVP8dVEqtt2
d4IbRyyXulFwLEeZVnD1B77P159CgV9fEpEmQjPMnNinINyvhOHWIlif8GZC6Anm
IOB1RbQ59g08xjYrdvM/GHuoqXJCs+8oQs+79fYZnQUfLFQe9sNhocjXVKWf2zFJ
ZMNl+VHCyXFRhvhekRKG8Hp4TjIgCnVLefzwlR7udAH4h4LhWOW3j1WauwSF0Wt1
CwbB5o3B3FRS5MmChCw/sfVG/20hk+6ySjojAgMBAAECggEAemB24AhFJfEH6Dlf
/QpQATD2JXo5cHCuTzSqrYB0ewqeQkr5Ab4Q9PnOSvKrVH7cvNs8ohFffjg3fhvv
b2e2SUYzXVNEE0rmQ/WTnO/8M2H2bj2Hp4NHc6tRZ5C3HYBd0/Ur4pwafANPawjY
C6Zmwca1Z8YukqNltKNCCQS5DiI8BFWCzuqePNCfvdppN0sQJaWKqsJdA3Jwj1mP
Bd6qPOiXJajuYXWQoxCKozCLb90cenRhkNRC5GpaCM5g6xqVJW+VBJEuZPAjkxeX
miGyar4HL/55zNqFV75FZvwRge/rPNjlDMB8ZEkryNeWv3XVJrTrv0UcfGMyDzFM
NjQusQKBgQC53IlLOResicXx/FV1/HRz4qnMWZfjSQ498pPr8A/c2KQp/fBgTteW
VScPlelXCRwQ3KHB3AJYHlC9AI6SKhbSuo3MZIpXE7T6gd0xHjiNmjqSBdcyLxl6
3kuVsf+sXStM5574azETB8SMFwyoq40PAkGzoMYkeCPXd4Abf5VnPwKBgQCuKEJB
KAN1g67ZEOywM+EkZTUmHtEQlsFw3HAwbKbDijwbn4+JUcGEjEprpGnnDFDcJvL3
szsw2ELsAMskRpbqUf3Kk8zXUq9Q5vLCKfkh/Z4cyCxIQzN4DHcjdbbS7HcmVkSW
WrvMhuDLHgo71m6HddSaVAbVUG3UTwmFBAh4HQKBgBWiAajrwEGo141O3XOaKsPC
Qhky5Gbj/fBf56+yhWYjIRhyIiRTiOxKhP1faYVj3gxoYbt6rBstjCAzjGSe2YE1
jYOYwDFabdoqe2BYMCTrKp4MZ/vDV6fhb9LAoQ2i2oNdAjfP4ipg4ROdKzAGp6hz
jsolkGp2QVW25wZMV0tpAoGAS4yvYTCIf5wGZ6fN5Yo76tv0uHq52uZrOBiImpkn
pr/630jSrZFHz8ZEKnoCbvaKxVYoJIgd70yBi3u0pCHzKeczn4OKYwY9g20Mdmpa
5wHsazPy8c4lL7jInhtcmhd2gKz/x/HIcis4rSR08AxPmnflKKW26Sag3m8DBC8B
tYkCgYBO6WVub7Tkw59YA6bWRd6d3CshY8UNur8V4PW/SxmS2WP+0tnYVLYUyBJ5
HreZaaX2q1SV6F86FTgF5E9ai1IBWZyx63Dqaa1HfBPED2oA+sgQHxHAveMKRB95
vH74pRKQpUPS2HxpkH0kBUoZK+ewrwN+6BTDnRNz9Nt/YvRt+A==
-----END RSA PRIVATE KEY-----
'''

##############  Conhecendo as funções do JWT ##############

payload = {'usuario':'felipe', 'permissoes':'admin'}

jwt_token = jwt.encode(payload, key=chave_privada, algorithm='RS256')
print(jwt_token)

print('-------------')

dados_do_token = jwt.decode(jwt_token, key=chave_publica, algorithms=['RS256'])
print(dados_do_token)

##########################################################

def nao_autenticado():
    raise HTTPException (
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Token incorreto',
        headers={"WWW-Authenticate": "Bearer"}
    )

def nao_autorizado():
    raise HTTPException (
        status_code=status.HTTP_403_FORBIDDEN,
        detail='Permissões incorretas',
        headers={"WWW-Authenticate": "Bearer"}
    )

def confere_token(req: Request):
    try:
        tipo_auth, token = req.headers['Authorization'].split()
        if tipo_auth != 'Bearer':
            nao_autenticado()
    except:
        nao_autenticado()
    print(token)
    try:
        dados_token = jwt.decode(token, key=chave_publica, algorithms=['RS256'])
    except:
        nao_autenticado()
    return dados_token

def valida_autorizacoes(dados_token: dict = Depends(confere_token)):
    print(dados_token.get('permissoes'))
    if dados_token.get('permissoes') == 'admin':
        return True
    nao_autorizado()

# Retorna o nome do usuário se este estiver autenticado,
# caso contratio retorna status 401
@app.get("/auth/token")
def token(usuario: str = Depends(confere_token)):
    return "Usuário autenticado: " + usuario.get('usuario')

# Retorna msg se o usuário estiver autenticado e autorizado,
# caso contratio retorna:
# Não autenticado: status 401
# Não autorizado:  status 403
@app.get("/muda/produto")
def token(autorizado: bool = Depends(valida_autorizacoes)):
    return "Nova quantidade de produto "