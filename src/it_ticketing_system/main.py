from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from src.it_ticketing_system.controllers import users, tickets

app = FastAPI(
    title="IT Ticketing System API",
    version="1.0.0",
    description="Backend para gerenciamento de chamados de TI"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health", tags=["Health Check"])
async def health_check():
    return {"status": "ok"}

app.include_router(users.router)
app.include_router(tickets.router)

if __name__ == "__main__":
    uvicorn.run("src.it_ticketing_system.main:app", host="0.0.0.0", port=8000, reload=True)
