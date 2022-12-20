import time


def calculate_time(func):
    def calculate(*args, **kwargs):
        start = time.process_time()
        result = func(*args, **kwargs)
        end_time = time.process_time() - start
        time_taken_in_ms = end_time * 1000
        print(f'time taken(ms): {float(round(time_taken_in_ms, 6))}')
        return result
    return calculate
