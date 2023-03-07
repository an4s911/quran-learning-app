class Queue:

    def __init__(self, pop_limit=1, lesser_urgent=None):
        self.queue = []
        self.popped_count = 0

        self.pop_limit = pop_limit
        self.lesser_urgent = lesser_urgent

    def push(self, item):
        self.queue.insert(0, item)

    def pop(self):
        if not self.queue:
            return self.lesser_urgent.pop() if self.lesser_urgent else None

        if self.lesser_urgent:
            if self.popped_count < self.pop_limit:
                self.popped_count += 1
                return self.queue.pop()
            else:
                self.popped_count = 0
                return self.lesser_urgent.pop()
        else:
            return self.queue.pop()


less_urgent = Queue()
normal = Queue(pop_limit=2, lesser_urgent=less_urgent)
urgent = Queue(pop_limit=3, lesser_urgent=normal)

today = []


def stack():
    while today.__len__() < 3:
        next_item = urgent.pop()
        if next_item:
            today.append(next_item)
        else:
            break
