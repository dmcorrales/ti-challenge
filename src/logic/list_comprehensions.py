

def get_even_integers(list_elements: list):
    yield list(filter(lambda x : x % 2 == 0, list_elements))
    yield [i for i in list_elements if i % 2 != 0]

if __name__ == '__main__':
    w = get_even_integers([1,2,3,4,5,6,7,8.1,9,10.11])
    print(next(w))
    print(next(w))
