from celery.utils.log import get_task_logger

from nss.celery import app
from .emails import send_delay_info_email

logger = get_task_logger(__name__)

@app.task(name="send_delay_info_email_task")
def send_delay_info_email_task(context: dict):
    delay = context["connection_delay"]
    logger.info(f"Sent delay info email. Delay is {delay}")
    
    return send_delay_info_email(context)
