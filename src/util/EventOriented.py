class Event:
    def __init__(self):
        self._events = {}
    
    def on(self, name, action):
        if name not in self._events.keys():
            self._events[name] = []
        self._events[name].append(action)

    def off(self, name, action):
        self._events[name].remove(action)
    

    def emit(self, name, paramns):
        for _item in self._events[name]:
            _item(paramns)
