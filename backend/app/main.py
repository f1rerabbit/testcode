from fastapi import FastAPI

app = FastAPI(title="My SaaS API")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {
        "service": "my-saas-api",
        "version": "0.1.0",
    }
