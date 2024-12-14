import logging

def setup_logging():
    logging.basicConfig(filename='migration.log', level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s', filemode='w')
    logging.info("Logging setup completed successfully.")