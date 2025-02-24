import random
def fill_list():
    lst = []
    for _ in range(10):
        lst.append(random.randint(1, 100))
    return lst

def generate_list():
    return [random.randint(1, 100) for _ in range(10)]
