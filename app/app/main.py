import sys
from typing import Any, Dict

from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext

logger = Logger()

def handler(event: Dict[str, Any], context: LambdaContext):
    logger.debug("logged!")
    return "Hello from AWS Lambda using Python" + sys.version + "!"