
from main import load_data, save_data, Queue
from console import print_line_in_box

print_line_in_box(
    "Converting data file from using old urgency lists to the new ones...")

print_line_in_box("Loading old data...")

data = load_data()
try:
    today_schedule_old = data['today_schedule']
    urgent = data['urgent']
    normal = data['normal']
    less_urgent = data['less_urgent']

    print_line_in_box("Loaded old data...")
except KeyError:
    print_line_in_box("Please make sure you have the right file")
    exit()

print_line_in_box("Creating new data object...")

list4 = Queue("4")
list3 = Queue("3", pop_limit=6, lesser_urgent=list4)
list2 = Queue("2", pop_limit=2, lesser_urgent=list3)
list1 = Queue("1", pop_limit=3, lesser_urgent=list2)

new_data = {
    'today_schedule': Queue('today_schedule'),
    '1': list1,
    '2': list2,
    '3': list3,
    '4': list4,
    'latest': None
}

today_schedule_new = new_data['today_schedule']

print_line_in_box("Created new data object...")

print_line_in_box(
    "Transferring data from old data object to new data object...")

for i in today_schedule_old:
    today_schedule_new.push(i, append=True)

print("old today schedule: ")
print(today_schedule_old)
print("new today schedule: ")
print(today_schedule_new)

for i in urgent:
    list1.push(i, append=True)

print(urgent)
print(list1)

for i in normal:
    list2.push(i, append=True)

print(normal)
print(list2)

for i in less_urgent:
    list3.push(i, append=True)

print(less_urgent)
print(list3)

print("list4")
print(list4)

print_line_in_box("Transferring done...")

print_line_in_box("Saving new data...")

save_data(new_data)

print_line_in_box("Saving done...")

print_line_in_box("Converting completed")
