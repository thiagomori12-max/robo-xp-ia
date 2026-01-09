from fastapi import FastAPI

app = FastAPI()

@app.get("/api/dashboard")
def dashboard():
    return {
        "robo": "ativo",
        "modo": "monitoramento",
        "perfil": "Conservador",
        "capital_inicial": 1000,
        "status": "Seguro - não opera dinheiro"
    }
