# Fastapi App Endpoint section
# Imprt fastAPI main class
from fastapi import FastAPI
# Import routers (these will be in  app/routers/folder)
from app.routers import upload , search , notify

# creating FastAPI  app instance 
app = FastAPI(title="Documetro AI" , Version = "1.0")


# Resgister routers (connect different route fies to main app )
# 'prefix means all routes inside that router will start with this path 
# EXample:POST /upload -> handled by upload.py
 
app.include_router(upload.router,prefix="/upload",tags=["Upload"])
app.include_router(search.router,prefix="/search",tags=["Search"])
app.include_router(notify.router,prefix="/notify",tags=["Notifications"])
# root route -> GET /
@app.get("/")
def root():
    return {"Message":"Documetro AI Backend is running..."}