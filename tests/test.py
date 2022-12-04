from EventEmitter.emits import EventEmitter

emits = EventEmitter()


def test_emits():
    results = {}

    def callback(data):
        results[data] = True
        if results.__len__() == 4:
            print(results)
            assert True

    emits.on("test add_event_listener", callback)
    emits.emit("test add_event_listener", "test data")

    emits.remove_event_listener("test remove_event_listener")
    emits.emit("test remove_event_listener", "test data")

    emits.on("test event", callback)
    emits.emit("test event", "test data")

    emits.once("test event once", callback)
    emits.emit("test event once", "test once data")
    emits.emit("test event once", "test once data2")

    emits.once("test event once", callback)
    emits.emit("test event once", "test once data3")

    emits.off("test event")
    emits.emit("test event", "test data")
