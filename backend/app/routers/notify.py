# importing modules and libraries

from fastapi import APIRouter

# Initialize the router for notification-related endpoints
router = APIRouter()

# notify endpoint

@router.post("/notify")
async def send_notification(message:str):
    # This endpoint sends notification of uploads .
    #  """
    # Send a notification (mock).
    # Later we will connect this to email/alerts service.
    # """
    return{"message":"Notification Sent"}