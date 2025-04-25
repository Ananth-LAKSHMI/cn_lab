def stop_and_wait(frames):
    for i, frame in enumerate(frames):
        print(f"Sending frame {i}")
        print(f"Acknowledgment for frame {i} received\n")

stop_and_wait(["A", "B", "C"])

def go_back_n(window_size):
    for i in range(0, 10, window_size):
        print(f"Sending frames {i} to {i+window_size-1}")
        print("ACK lost! Resending all...\n")

go_back_n(3)


received = [True, False, True, True]

for i, ack in enumerate(received):
    if not ack:
        print(f"Frame {i} not acknowledged. Resending...")
    else:
        print(f"Frame {i} acknowledged.")

OUTPUT:


Sending frame 0
Acknowledgment for frame 0 received

Sending frame 1
Acknowledgment for frame 1 received

Sending frame 2
Acknowledgment for frame 2 received

Sending frames 0 to 2
ACK lost! Resending all...

Sending frames 3 to 5
ACK lost! Resending all...

Sending frames 6 to 8
ACK lost! Resending all...

Sending frames 9 to 11
ACK lost! Resending all...

Frame 0 acknowledged.
Frame 1 not acknowledged. Resending...
Frame 2 acknowledged.
Frame 3 acknowledged.
