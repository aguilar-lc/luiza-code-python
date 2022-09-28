from fastapi import FastAPI, Depends, status, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
seguraca = HTTPBasic()

def confere_credencial(credencial: HTTPBasicCredentials = Depends(seguraca)):
    usuario = 'felipe'
    senha = 'luizacode'

    credencial_usuario = credencial.username
    credencial_senha = credencial.password

    if usuario == credencial_usuario:
        if senha == credencial_senha:
            return credencial_usuario
   
    raise HTTPException (
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='Usuário ou Senha incorretos',
        headers={"WWW-Authenticate": "Basic"}
    )

@app.get("/auth/basic")
def basic(usuario: str = Depends(confere_credencial)):
    return "Retornar o produto X"