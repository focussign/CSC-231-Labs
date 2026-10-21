import sys
import time
from treemap import TreeMap


def binary_search(lst, item):
    first = 0
    last = len(lst) - 1
    found = None
    while first <= last and not found:
        midpoint = (first + last) // 2
        if lst[midpoint] == item:
            found = midpoint
        else:
            if item < lst[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


def format_time(t):
    return f'{t * 1000:.2f}ms'


class UserInfo:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def __str__(self):
        return f"username: {self.username}, password: {self.password}"

    def __eq__(self, other):
        return self.username == other.username and self.password == other.password

    def __lt__(self, other):
        return self.username < other.username

    def __gt__(self, other):
        return self.username > other.username

    def __repr__(self):
        return f"UserInfo({self.username}, {self.password})"


def seq_search(filename):
    user_lst = []
    print("-" * 5)
    print("Loading usernames and passwords from", filename, "into a Python list[] using append()")
    start = time.perf_counter()
    with open(filename) as file:
        for line in file:
            username, password = line.strip().split(',')
            user_lst.append(UserInfo(username, password))
    print('Time to store:', format_time(time.perf_counter() - start))

    print("Now, we will use a sequential search to look for users in the list[].")
    done = False
    while not done:
        username = input("Enter username, or leave blank to go back: ")
        if username == '':
            done = True
            continue
        password = input("Password (capitalization matters): ")
        user = UserInfo(username, password)
        start = time.perf_counter()
        if user in user_lst:
            print('Valid credentials found!')
        else:
            print('Invalid credentials')
        print('Time to search:', format_time(time.perf_counter() - start))


def bin_search(filename):
    user_lst = []
    print("-" * 5)
    print("Loading usernames and passwords from", filename, "into a Python list[] using append()")
    start = time.perf_counter()
    with open(filename) as file:
        for line in file:
            username, password = line.strip().split(',')
            user_lst.append(UserInfo(username, password))
    print('Time to store:', format_time(time.perf_counter() - start))

    print('Now sorting the list (this could take a while for bigger files)...')
    start = time.perf_counter()
    user_lst.sort()
    print('Time to sort to the list[]:', format_time(time.perf_counter() - start))

    print("Now, we will use a binary search to look for users in the list[].")
    done = False
    while not done:
        username = input("Enter username, or leave blank to go back: ")
        if username == '':
            done = True
            continue
        password = input("Password (capitalization matters): ")
        user = UserInfo(username, password)

        start = time.perf_counter()
        first = 0
        last = len(user_lst) - 1
        found = False
        while first <= last and not found:
            midpoint = (first + last) // 2
            if user_lst[midpoint] == user:
                found = True
            else:
                if user < user_lst[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1

        if found:
            print('Valid credentials found!')
        else:
            print('Invalid credentials')
        print('Time to search:', format_time(time.perf_counter() - start))


def bst(filename):
    creds = TreeMap()
    print("-" * 5)
    print("Storing usernames and passwords from", filename,
          "into your TreeMap. Usernames will be keys and passwords will be values.")
    print("This might take a while for the bigger files...")
    start = time.perf_counter()
    with open(filename) as file:
        for line in file:
            username, password = line.strip().split(',')
            creds[username] = password
    print('Time to store:', format_time(time.perf_counter() - start))
    print(f"The binary search tree data structure has height: {creds.height()}")
    print(
        f"The binary search tree is taking up approximately {sys.getsizeof(creds.root) * creds.size} bytes of memory.")

    print("Now, lookup credentials using the Map interface.")
    done = False
    while not done:
        username = input("Enter username, or leave blank to go back: ")
        if username == '':
            done = True
            continue
        password = input("Password (capitalization matters): ")
        start = time.perf_counter()
        if username in creds and creds[username] == password:
            print('Valid credentials found!')
        else:
            print('Invalid credentials')
        print('Time to search:', format_time(time.perf_counter() - start))


if __name__ == "__main__":
    files = {
        '1': 'users_250000.csv',
        '2': 'users_1000000.csv',
        '3': 'users_5000000.csv'
    }

    algs = {
        '1': seq_search,
        '2': bin_search,
        '3': bst,
    }

    while True:
        print("\nWelcome to the LogItIn Credentials checker! (Very exciting)")
        print("Which users file do you want to load?")
        print("1) users_250000.csv (population of Durham, NC)")
        print("2) users_1000000.csv (population of Rhode Island)")
        print("3) users_5000000.csv (population of South Carolina)")
        file_choice = input("Enter your selection, or leave blank to quit: ")
        if file_choice == '':
            print("Goodbye!")
            exit(0)

        if file_choice not in files:
            print("I don't understand that selection. Please pick a number [1-3]")
            exit(1)

        print("How do you want to search them?")
        print("1) Python list[] with sequential search")
        print("2) Sorted Python list[] with binary search")
        print("3) Your TreeMap that uses a binary search tree")
        alg_choice = input("Enter your selection, or leave blank to quit: ")
        if alg_choice == '':
            print("\nGoodbye!")
            exit(0)

        if alg_choice not in algs:
            print("I don't understand that selection. Please pick a number [1-3]")
            exit(1)

        algs[alg_choice](files[file_choice])
