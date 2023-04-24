from app.controller import run

import logging
from logging import handlers

import signal
import sys
import atexit

if __name__ == "__main__":
    log = logging.getLogger('')
    log.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    log.addHandler(ch)

    fh = handlers.RotatingFileHandler(
        'deku.log', maxBytes=(1048576*5), backupCount=7)
    fh.setFormatter(formatter)
    log.addHandler(fh)

    run()
