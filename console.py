from main import Queue
from main import get_today_schedule, restack_today, get_lists, get_list
from main import remove_item_from_list, get_next_card
from main import add_item as add_item_to_list

urgencies = {
    't': 'today_schedule',
    'u': 'urgent',
    'n': 'normal',
    'l': 'less_urgent'
}


def show_today():
    today_schedule = get_today_schedule()

    print("\n" + "-"*20)
    print("| Today's Schedule |")
    print("-"*20 + "\n")
    if today_schedule.__len__() == 0:
        print("Schdule is empty")
        print("Restack and try again...")
    else:
        for item in today_schedule.queue:
            print(item)

    print("\n" + "*"*20 + "\n")


def add_item(item_name=None):
    if not item_name:
        item_name = input("Name: ")

    print("(U)rgent\n(N)ormal\n(L)ess Urgent")
    urgency_choice = input(": ").lower()

    match urgency_choice:
        case 'u' | 'n' | 'l':
            try:
                add_item_to_list(item_name, urgencies[urgency_choice])
            except ValueError:
                print("Item already exists in list")

        case _:
            print("Invalid choice")
            return


def show_lists():
    lists = get_lists()

    for item in lists:
        print(item)


def show_next():
    today_schedule = get_today_schedule()
    next_card = get_next_card()

    if not next_card:
        print("No next card")
        return

    print_line_in_box("Current Card: " + next_card)
    input("Press Enter to continue...")
    print("Add card to list")

    add_item(next_card)


def print_line_in_box(line: str):
    length = line.__len__() + 10
    print('-' * length)
    print('|' + line.center(length - 2, ' ') + '|')
    print('-' * length)


def advanced():
    print("Advanced")
    print("(R)emove item")
    choice = input(": ").lower()

    match choice:
        case 'r':
            show_lists()
            list_choice = urgencies[input("(T) / (U) / (N) / (L): ").lower()]
            list_items = get_list(list_choice)

            for num, item in enumerate(list_items.queue, start=1):
                print(f"{num}. {item}")

            choice_num = int(input(": ")) - 1
            remove_item_from_list(list_choice, choice_num)


def main():
    print("Quran Memoriation")

    while True:
        print('='*5 + "MENU" + '='*5)
        print("1. Today")
        print("2. Next")
        print("3. Restack")
        print("4. Add")
        print("5. Lists")
        print("0. Exit")
        print("-"*14)
        print("6.advanced")

        choice = int(input(": "))

        match choice:
            case 1:
                show_today()

            case 2:
                show_next()

            case 3:
                restack_today()

            case 4:
                add_item()

            case 5:
                show_lists()

            case 6:
                advanced()

            case 0:
                break

            case _:
                print("Invalid choice")

        input("Press Enter to continue...")
        print('-'*20)


if __name__ == '__main__':
    main()