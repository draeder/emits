from EventEmitter.emits import EventEmitter

events = EventEmitter()


def test_emits():
    results = {}

    def callback(data):
        results[data] = True
        if results.__len__() == 4:
            print(results)
            assert True

    events.on("test add_event_listener", callback)
    events.emit("test add_event_listener", "test data")

    events.remove_event_listener("test remove_event_listener")
    events.emit("test remove_event_listener", "test data")

    events.on("test event", callback)
    events.emit("test event", "test data")

    events.once("test event once", callback)
    events.emit("test event once", "test once data")
    events.emit("test event once", "test once data2")

    events.once("test event once", callback)
    events.emit("test event once", "test once data3")

    events.off("test event")
    events.emit("test event", "test data")
