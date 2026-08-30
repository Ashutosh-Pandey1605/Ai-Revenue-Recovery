from fastapi import FastAPI

app = FastAPI(title="Revenue Recovery API")


@app.get("/health")
def health_check():
    return {"status": "ok"}