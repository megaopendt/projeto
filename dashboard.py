from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def home():
    return {"status": "Rodando!", "saldo": get_balance()}
