import time
import logging
from functools import wraps

def retry_on_timeout(max_attempts=2, wait_seconds=5):
    """
    A decorator to retry a function upon encountering an exception.

    :param max_attempts: Maximum number of attempts (default is 2).
    :param wait_seconds: Number of seconds to wait before retrying (default is 5 seconds).
    """

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Get the number of retries from kwargs if provided, otherwise use max_attempts
            attempts = kwargs.pop('retries', max_attempts)

            for attempt in range(attempts):
                try:
                    # Try to execute the function
                    return func(*args, **kwargs)
                except Exception as ex:
                    # Log the exception and retry
                    logging.exception(f"The exception raised while executing the function is: {ex}")
                    logging.info(f"Attempt {attempt + 1} failed, retrying in {wait_seconds} seconds...")
                    time.sleep(wait_seconds)

            # If all attempts fail, raise the last exception
            logging.error(f"All {attempts} attempts failed.")
            raise Exception(f"Function {func.__name__} failed after {attempts} attempts")

        return wrapper

    return decorator
