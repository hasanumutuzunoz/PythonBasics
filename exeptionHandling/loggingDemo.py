# Alt+Shift+Up or Alt+Shift+Down changes the code line

import logging

# Write the error into a file with level error and higher
logging.basicConfig(filename="myLog.log", level=logging.INFO)

logging.critical("critical") # Highest level
logging.error("Error has occured at line xxxx")
logging.warning("warning") # Default log level is warning
logging.info("info") # Below than warning so we cannot see
logging.debug("debug")
