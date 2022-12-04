# emits
> A simple Event Emitter for Python

## Install
```commandline
pip install emits
```

## Usage
```python
from emits import EventEmitter

emits = EventEmitter()
```

## API
### `emits.on(event_name, callback)` or `emits.add_event_listner(event_name, callback)`
Register an event listener for the given `event_name` which uses the defined callback function to consume the data it receives

#### Example
```python
def callback(data):
    print(data)

emits.on("my event", callback)
emits.add_event_listener("my event", callback)
```

### `emits.once(event_name, callback)` or `emits.add_event_listener_once(event_name, callback)`
Register an event listener for the given `event_name` which uses the defined callback function to consume the data it receives only once

### `emits.off(event_name)` or `emits.remove_event_listener(event_name)`
Turn off an event listener created by `emits.on()` or `emits.add_event_listener()`

