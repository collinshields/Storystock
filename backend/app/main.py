from fastapi import FastAPI

app = FastAPI(title="Storystock")


@app.get("/")
def root():
    return {"message": "I am running yaya"}