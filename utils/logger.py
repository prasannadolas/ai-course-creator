import logging
import sys

def setup_logger(name="AI_Course_Creator"):
    """
    Configures a professional logger that prints to the console.
    """
    logger = logging.getLogger(name)
    
    # If logger already has handlers, don't add them again (prevents duplicate logs)
    if logger.hasHandlers():
        return logger
        
    logger.setLevel(logging.INFO)

    # Create console handler
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)

    # Create formatter (Time - Level - Message)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

# Initialize a default logger instance
app_logger = setup_logger()