from fastapi import FastAPI

from app.routes import router

app = FastAPI(title="Gateway API")

app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.2", port=8000, reload=True)
