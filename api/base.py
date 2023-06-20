from fastapi import APIRouter
from utils import base as baseUtils

router=APIRouter(    
	prefix="/base",
	tags=["base"]
)

@router.get("/check-env")
def get_env():
    return  baseUtils.get_env()
