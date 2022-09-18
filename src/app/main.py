import logging
from os import getenv

import app

logging.basicConfig(level=logging.INFO)
logging.getLogger('aiogram').propagate = False


if __name__ == "__main__":
    app.main(getenv('token'))
