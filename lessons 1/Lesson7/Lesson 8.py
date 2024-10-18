import logging


# logging.basicConfig(level=logging.DEBUG)
# logging.debug("Debug")
# logging.info("Info")
# logging.warning("Warning")
# logging.error("Error")
# logging.critical("Critical")
#
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("Debug1")
# logging.info("Info1")

logging.basicConfig(level=logging.DEBUG,
                    filename="logs.log",
                    filemode="w",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# logging.debug("Debug")
# logging.info("Info")

try:
    print(5/0)
except ZeroDivisionError:
    logging.exception("ZeroDivisionError")
