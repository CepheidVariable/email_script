from os.path import dirname, abspath
import logging

ROOT_DIR = dirname(abspath(__file__))

logging.basicConfig(
    level= logging.INFO,
    format='%(date)s %(asctime)s - %(levelname)s: %(message)s'
)