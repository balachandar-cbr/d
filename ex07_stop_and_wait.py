# Ex 7: Stop-and-Wait Protocol
import time

def stop_and_wait(frames):
    for i in range(1, frames + 1):
        while True:
            print(f"\nSender: Sending Frame {i}")
            time.sleep(1)
            print(f"Receiver: Frame {i} received successfully")
            time.sleep(1)
            ack = input(f"Enter ACK for Frame {i} (Y/N): ").upper()
            if ack == 'Y':
                print(f"Sender: ACK {i} received")
                print(f"Frame {i} transmitted successfully")
                break
            else:
                print(f"Sender: ACK {i} lost")
                print(f"Sender: Retransmitting Frame {i}")
    print("\nAll frames transmitted successfully.")

n = int(input("Enter the number of frames: "))
stop_and_wait(n)
