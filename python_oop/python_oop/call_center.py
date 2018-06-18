import uuid
from datetime import datetime

class Call(object):
    def __init__(self, name, phone_number,reason, call_time=None):
        self.id = uuid.uuid4()
        self.name = name
        self.phone_number = phone_number
        self.call_time = call_time if call_time else datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.reason = reason

    def display(self):
        print("The id %s which name %s was called in %s because of  %s" % (self.id,
                                                                           self.name,
                                                                           self.call_time,
                                                                           self.reason))

class CallCenter(object):
    def __init__(self):
        self.calls = list()
        self.queue_size = len(self.calls)

    def add(self, new_call):
        self.calls.append(new_call)
        # need to be sorted firstly
        self.calls = sorted(self.calls, key=lambda x: x.call_time)

    def remove(self):
        try:
            del self.calls[0]
        except Exception:
            print("We don't have any call to remove")

    def info(self):
        for call in self.calls:
            call.display()


#testing to create a custom datetime
# datetime(2018,9,9,12,15,33).strftime('%Y-%m-%d %H:%M:%S')
# the output '2018-09-09 12:15:33'

