import threading
import time
import random
from queue import PriorityQueue


class Producer:
    def __init__(self, priority_queue):
        self.priority_queue = priority_queue

    def produce(self, num_items):
        for _ in range(num_items):
            priority = random.randint(1, 10)  # Random priority between 1 and 10
            item = f"item-{random.randint(1, 100)}"
            print(f"Producer producing {item} with priority {priority}")
            self.priority_queue.put((priority, item))
            time.sleep(random.random())  # Simulate production time


class Consumer(threading.Thread):
    def __init__(self, name, priority_queue):
        threading.Thread.__init__(self)
        self.name = name
        self.priority_queue = priority_queue

    def run(self):
        while True:
            try:
                priority, item = self.priority_queue.get(timeout=5)  # Wait for item with a timeout of 5 seconds
                print(f"Consumer {self.name} consuming {item} with priority {priority}")
                self.priority_queue.task_done()  # Indicate that the item has been processed
                time.sleep(random.random())  # Simulate consumption time
            except:
                break  # Exit if no item is received within the timeout

def main():
    priority_queue = PriorityQueue()  # Create a thread-safe priority queue
    producer = Producer(priority_queue)
    # Run the producer in the main thread
    # Create and start consumer threads
    consumers = [Consumer(f"C{i}", priority_queue) for i in range(5)]
    for consumer in consumers:
        consumer.start()


    producer.produce(20)  # Produce 20 items

    # Wait until all items have been processed
    priority_queue.join()

    # Ensure all consumers finish processing
    for consumer in consumers:
        consumer.join()


if __name__ == "__main__":
    main()
