# error_handler.py
def handle_error(error_message):
    """Print and log errors."""
    print(f"Error: {error_message}")
    from logger import log_error
    log_error(error_message)
