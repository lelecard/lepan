from fastapi import FastAPI


app = FastAPI(
    title="LePan API",
    version="1.0.0"
)


@app.get("/")
def root():

    return {
        "project": "LePan",
        "status": "running"
    }


@app.get("/health")
def health():

    return {
        "health": "ok"
    }
