from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class AccountCreate(BaseModel):
    owner: str
    balance: int = 0

accounts: dict[int, dict] = {}
next_id: int = 1

@app.post("/accounts/", status_code=201)
def create_account(data: AccountCreate):
    global next_id
    account = {"id": next_id, "owner": data.owner, "balance": data.balance}
    accounts[next_id] = account
    next_id += 1
    return account

@app.get("/accounts/{account_id}")
def get_account(account_id: int):
    account = accounts.get(account_id)
    if not account:
        raise HTTPException(status_code=404, detail="Account not found")
    return account