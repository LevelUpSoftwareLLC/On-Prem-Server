import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1  # Dynamically scale workers
bind = '127.0.0.1:8000'  # Listen on all network interfaces on port 8000
accesslog = '-'  # Log access to stderr
errorlog = '-'  # Log errors to stderr
