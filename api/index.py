import asyncio
from mangum import Mangum
from app.main import app

# Create the Mangum adapter for ASGI apps
handler = Mangum(app)


def main(event, context):
    """
    AWS Lambda handler for the FastAPI application.
    This is needed for Vercel's serverless functions.
    """
    return handler(event, context)


# For Vercel deployment
app_handler = handler

# Export handler for Vercel
def handler_func(event, context):
    return handler(event, context)