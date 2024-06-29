import psutil
import logging

# Set thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

# Configure logging
logging.basicConfig(filename='system_health.log', level=logging.INFO)

def check_cpu():
    usage = psutil.cpu_percent(interval=1)
    if usage > CPU_THRESHOLD:
        logging.warning(f'High CPU usage: {usage}%')

def check_memory():
    usage = psutil.virtual_memory().percent
    if usage > MEMORY_THRESHOLD:
        logging.warning(f'High Memory usage: {usage}%')

def check_disk():
    usage = psutil.disk_usage('/').percent
    if usage > DISK_THRESHOLD:
        logging.warning(f'High Disk usage: {usage}%')

def check_processes():
    processes = [p.info for p in psutil.process_iter(attrs=['pid', 'name'])]
    logging.info(f'Running processes: {processes}')

if __name__ == '__main__':
    check_cpu()
    check_memory()
    check_disk()
    check_processes()
