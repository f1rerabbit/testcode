from fastapi import FastAPI

app = FastAPI(title="My SaaS API")

@app.get("/health")
def health():
    return {"status": "ok"}
