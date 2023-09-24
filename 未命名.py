import random
import time

def generate_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return ''.join(random.choice(letters) for i in range(length))

def generate_random_number(digits):
    return random.randrange(10**(digits-1), 10**digits)

def print_progress_bar(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()

items = []
for i in range(5000):
    
    items.append({
        'id': generate_random_number(10),
        'name': generate_random_string(20),
        'description': generate_random_string(100),
        'price': random.random() * 100,
        'quantity': random.randint(0, 100)
    })

print("Generating random dataset...")
for i, item in enumerate(items):
    print_progress_bar(i + 1, len(items), prefix = 'Progress:', suffix = 'Complete', length = 50)
    time.sleep(0.01)

print("Dataset generated.")

def bulk_insert(items):
    print("Inserting items into database...")
    for i, item in enumerate(items):
        print_progress_bar(i + 1, len(items), prefix = 'Progress:', suffix = 'Complete', length = 50)
        time.sleep(0.01)
        # Database insert code here
        pass
    print("Items inserted.")

bulk_insert(items)

print("Done!")
