from EventEmitter.emits import Events

events = Events()


def listen():
    def callback(data):
        print(data)


    events.on("test event", callback)
