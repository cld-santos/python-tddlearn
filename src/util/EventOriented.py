class Event:
    _events = {}
    
    def on(self, name, action):
        if name not in self._events.keys():
            self._events[name] = []
        self._events[name].append(action)

    def emit(self, name):
        for _item in self._events[name]:
            _item()
