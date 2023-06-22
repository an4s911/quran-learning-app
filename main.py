from pickle import dump, load

FILENAME = 'data.pkl'


class Queue:

    def __init__(self, name: str, pop_limit=1, lesser_urgent=None):
        self.queue = []
        self.popped_count = 0

        self.name = name

        self.pop_limit = pop_limit
        self.lesser_urgent = lesser_urgent

    def __str__(self):
        return f"{self.name.capitalize()}: {str(self.queue)}"

    def __len__(self):
        return len(self.queue)
    
    def __bool__(self):
        return True

    def __getitem__(self, item: int):
        return self.queue[item]

    def push(self, item, append=False):
        if item in self.queue:
            raise ValueError(f"{item} is already in the queue")

        if not append:
            self.queue.insert(0, item)
        else:
            self.queue.append(item)

    def pop(self, index=-1):
        if not self.queue:
            return self.lesser_urgent.pop(index) if self.lesser_urgent else None

        if self.lesser_urgent:
            if self.popped_count < self.pop_limit:
                self.popped_count += 1
                return self.queue.pop(index)
            else:
                self.popped_count = 0
                return self.lesser_urgent.pop(index)
        else:
            return self.queue.pop(index)


def add_item(item, urgency_list: str, new=False):
    data = load_data()

    try:
        data[urgency_list].push(item)
    except KeyError:
        raise KeyError(f'Urgency list {urgency_list} does not exist')
    else:
        if new:
            data['latest'] = item

    save_data(data)


def remove_item_from_list(urgency_list: str, index=-1):
    data = load_data()

    try:
        data[urgency_list].pop(index)
    except KeyError:
        raise KeyError(f'Urgency list {urgency_list} does not exist')

    save_data(data)

def get_latest_item():
    data = load_data()

    return data['latest']


def save_data(data: dict):
    dump(data, open(FILENAME, 'wb+'))


def load_data() -> dict:
    try:
        data = load(open(FILENAME, 'rb'))
    except FileNotFoundError:
        list4 = Queue("4")
        list3 = Queue("3", pop_limit=5, lesser_urgent=list4)
        list2 = Queue("2", pop_limit=2, lesser_urgent=list3)
        list1 = Queue("1", pop_limit=3, lesser_urgent=list2)

        data = {
            'today_schedule': Queue('today_schedule'),
            '1': list1,
            '2': list2,
            '3': list3,
            '4': list4,
            'latest': None
        }

        save_data(data)

    return data


def restack_today(limit=3):
    data = load_data()

    today_schedule = data['today_schedule']
    list1 = data['1']
    while today_schedule.__len__() < limit:
        next_item = list1.pop()
        if next_item:
            today_schedule.push(next_item, append=True)
        else:
            break

    save_data(data)


def get_today_schedule():
    data = load_data()

    return data['today_schedule']


def get_list(urgency_list: str) -> list:
    data = load_data()

    return data[urgency_list]


def get_lists():
    data = load_data()

    return [data[i] for i in data if type(data[i]) == Queue]


def get_next_card():
    data = load_data()

    today_schedule = data['today_schedule']

    next_item = today_schedule.pop(0)

    save_data(data)

    return next_item


def main():
    pass


if __name__ == "__main__":
    main()
