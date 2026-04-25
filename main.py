from fastapi import FastAPI

# Create the database tables

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello world!"}

@app.get("/health")
def health_check():
    return {"status": "online"}