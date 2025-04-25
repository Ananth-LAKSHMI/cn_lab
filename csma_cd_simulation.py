import random

def csma_cd():
    attempts = 0
    while True:
        attempts += 1
        print("Checking if line is idle...")
        if random.random() > 0.2:
            print("Transmitting data...")
            if random.random() < 0.1:
                print("Collision detected! Sending jamming signal...\n")
            else:
                print("Data sent successfully.\n")
                break

csma_cd()

OUTPUT:
Checking if line is idle...
Transmitting data...
Data sent successfully.
