import threading # Threading program that runs two programs at once

class Messaging(threading.Thread):
    def run(self):
        for _ in range(100):  # Placed _ because you need the loop not the value.
            print(threading.current_thread().getName())

x = Messaging(name='Send out messages.')
y = Messaging(name="Received Messages.")
x.start()  # This is how a thread is called.
y.start()  # Before x thread is finished running y thread is started.