def repeat(times, sentence):
    result = []
    for _ in range(times):
        result.append(sentence)
    return result

def display(l):
    print('\n'.join(l))

if __name__ == '__main__':
    display(repeat(100, "Hello World"))
