from fastapi import FastAPI
from routes import auth
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from database import db  # Ensure database connection is established

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Register router
app.include_router(auth.router, prefix="/auth")

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8601)