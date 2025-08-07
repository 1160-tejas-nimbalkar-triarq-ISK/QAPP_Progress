import logging
import os
from datetime import datetime
from pywinauto import Desktop


def before_all(context):
    """
    Set up the testing environment before all tests
    """
    # Create logger
    log_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "logs")
    os.makedirs(log_dir, exist_ok=True)
    
    log_filename = os.path.join(log_dir, f"glo_emr_test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log")
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_filename),
            logging.StreamHandler()
        ]
    )
    
    context.logger = logging.getLogger('environment')
    context.logger.info("Starting gloEMR test session")
    
    # Initialize desktop
    context.desktop = Desktop(backend="uia")
    context.logger.info("Desktop environment initialized")


def before_scenario(context, scenario):
    """
    Set up before each scenario
    """
    context.logger.info(f"Starting scenario: {scenario.name}")
    

def after_scenario(context, scenario):
    """
    Clean up after each scenario
    """
    context.logger.info(f"Finished scenario: {scenario.name} - Status: {scenario.status}")
    
    # Clean up any remaining processes
    try:
        if hasattr(context, 'glo_emr_process') and context.glo_emr_process:
            context.glo_emr_process.terminate()
            context.logger.info("Terminated gloEMR process")
    except Exception as e:
        context.logger.warning(f"Error terminating process: {e}")


def after_all(context):
    """
    Clean up after all tests
    """
    context.logger.info("gloEMR test session completed") 