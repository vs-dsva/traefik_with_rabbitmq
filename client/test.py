import stomp
import logging
import time

conn = stomp.Connection([('192.168.160.2', 61613)])
while True:
    print("Connecting...")
    conn.connect('guest', 'guest', wait=True)
    print("Sending...")
    conn.send(body='Boo!', destination='/queue/test')
    print("Disconnecting...")
    conn.disconnect()
    time.sleep(15)