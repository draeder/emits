class EventEmitter:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(EventEmitter, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.event_name = None
        self.message = None
        self.one_time = {}
        self.add_event_listener = self.on
        self.add_event_listener_once = self.once
        self.remove_event_listener = self.off

    callbacks = None

    def on(self, event_name, callback):
        self.event_name = event_name
        if self.callbacks is None:
            self.callbacks = {}

        if event_name not in self.callbacks:
            self.callbacks[event_name] = [callback]
        else:
            self.callbacks[event_name].append(callback)

    def once(self, event_name, callback):
        self.on(event_name, callback)
        self.one_time[event_name] = 0

    def off(self, event_name):
        if self.callbacks is not None and event_name in self.callbacks:
            self.callbacks.pop(event_name)

    def emit(self, event_name, message):
        def xmit():
            self.message = message

            if self.callbacks is not None and event_name in self.callbacks:
                for callback in self.callbacks[event_name]:
                    callback(message)
        if event_name in self.one_time:
            if self.one_time[event_name] == 0:
                xmit()
                self.one_time[event_name] += 1
                self.callbacks[event_name].pop()
        else:
            xmit()
