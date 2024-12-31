import time
import random

def apply_rate_limit(min_delay=1, max_delay=2):
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)
