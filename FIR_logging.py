import logging
import sys

log_file = '/home/sangharshmanuski/Documents/mha_FIRs/logging_files/logFile_7.log'

# logging - source: https://stackoverflow.com/questions/
# 13733552/logger-configuration-to-log-to-file-and-print-to-stdout
# Change root logger level from WARNING (default) to NOTSET in order for all messages to be delegated.
logging.getLogger().setLevel(logging.NOTSET)

# Add stdout handler, with level INFO
console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.INFO)
formater = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S")
console.setFormatter(formater)
logging.getLogger().addHandler(console)

# Add file handler, with level DEBUG
handler = logging.FileHandler(log_file)
handler.setLevel(logging.INFO)
formater = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', "%Y-%m-%d %H:%M:%S")
handler.setFormatter(formater)
logging.getLogger().addHandler(handler)

logger = logging.getLogger(__name__)

# this line will appear on console and in the log file
logger.info("Application started")


