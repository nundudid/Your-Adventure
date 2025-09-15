from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings

app = FastAPI(
	title="'Your Adventure' Game API",
	description="API to generate adventurous stories",
)

app.add_middleware(
	CORSMiddleware,
	allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn
    print(settings)
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
