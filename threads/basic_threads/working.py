import datetime
import random
import threading
import time

import colorama


def main():
    t0 = datetime.datetime.now()
    print(colorama.Fore.WHITE + "App started.", flush=True)
    data = []

    threads = [
        threading.Thread(target=generate_data, args=(20, data)),
        threading.Thread(target=generate_data, args=(20, data)),
        threading.Thread(target=process_data, args=(40, data)),
    ]

    [t.start() for t in threads]

    print("Started...")

    [t.join() for t in threads]


def generate_data(num: int, data: list):
    for idx in range(1, num + 1):
        item = idx * idx
        data.append((item, datetime.datetime.now()))

        print(colorama.Fore.YELLOW + f" -- generated item {idx}", flush=True)
        time.sleep(random.random() + 0.5)


def process_data(num: int, data: list):
    processed = 0
    while processed < num:
        item = None

        if data:
            item = data.pop(0)
        if not item:
            time.sleep(0.01)
            continue

        processed += 1
        value = item[0]
        t = item[1]
        dt = datetime.datetime.now() - t

        print(
            colorama.Fore.CYAN
            + f" +++ Processed value {value} after {dt.total_seconds():,.2f} sec.",
            flush=True,
        )
        time.sleep(0.5)


if __name__ == "__main__":
    main()
