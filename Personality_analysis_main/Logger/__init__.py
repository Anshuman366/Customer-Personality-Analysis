import logging
from datetime import datetime
import os


LOG_DIR='customer_logs'

current_time_stamp= f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

log_file=f"log_{current_time_stamp}.log"

os.makedirs(LOG_DIR,exist_ok=True)

file_path=os.path.join(LOG_DIR,log_file)

logging.basicConfig(filename=file_path,
                    filemode="w",
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

