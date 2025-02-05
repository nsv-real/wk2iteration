## https://betterstack.com/community/guides/logging/how-to-start-logging-with-python/
import logging
import sys

logger = logging.getLogger("app")
stdout = logging.StreamHandler(stream=sys.stdout)
fmt = logging.Formatter(
    "%(name)s: %(asctime)s | %(levelname)s | %(message)s"
)
stdout.setFormatter(fmt)
logger.addHandler(stdout)
logger.setLevel(logging.INFO)