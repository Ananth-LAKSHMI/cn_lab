def leaky_bucket(input_packets, bucket_size):
    bucket = 0
    for pkt in input_packets:
        if bucket + pkt > bucket_size:
            print("Packet dropped! Bucket overflow.")
        else:
            bucket += pkt
            print(f"Packet of size {pkt} accepted. Bucket: {bucket}")
        bucket = max(0, bucket - 1)  # Simulate drain

leaky_bucket([2, 3, 5, 1, 4], 6)


OUTPUT:

Packet of size 2 accepted. Bucket: 2
Packet of size 3 accepted. Bucket: 4
Packet dropped! Bucket overflow.
Packet of size 1 accepted. Bucket: 3
Packet of size 4 accepted. Bucket: 6
