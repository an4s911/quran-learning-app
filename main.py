from datetime import datetime
from pickle import dump, load


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


def stack(urgencies, day):
    while day.__len__() < 3:
        next_item = urgencies[0].pop()
        if next_item:
            day.append(next_item)
        else:
            break


def main():
    urgency_list_filename = 'urgencies.pickle'
    today_schedule_filename = 'today.pickle'

    try:
        urgent = load(open(urgency_list_filename, 'rb'))
    except FileNotFoundError:
        less_urgent = Queue()
        normal = Queue(pop_limit=2, lesser_urgent=less_urgent)
        urgent = Queue(pop_limit=3, lesser_urgent=normal)

        dump(urgent, open(urgency_list_filename, 'wb+'))
    else:
        normal = urgent.lesser_urgent
        less_urgent = normal.lesser_urgent

    try:
        today_schedule = load(open(today_schedule_filename, 'rb'))
    except FileNotFoundError:
        today_schedule = {
            'date': datetime.today().date(),
            'queue': [],
            'stacked': False
        }

        dump(today_schedule, open(today_schedule_filename, 'wb+'))


if __name__ == "__main__":
    main()
