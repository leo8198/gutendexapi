from fastapi import APIRouter


# Endpoint to handle the health check
router = APIRouter(
    prefix='/api/v1'
)

# Health checker endpoint
@router.get("/health")
async def health_checker():

    return {'detail':{
                'status':'ok',
                }
            }
