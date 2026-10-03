from fastapi import FastAPI

app = FastAPI(title="FastAPI Support IT Ticket")

@app.get("/health")
def health_check():
    return {
        "status":"OK"
    }

