def func(home, homeries):
    if home not in homeries:
        return 'HelloWorld'
    return homeries[home]


def displey(l):
    print(l)


if __name__ == '__main__':
    homeries = {
        'アメリカ': 'America',
        'カナダ': 'Canada',
        'タイ': 'Tailand',
        'メキシコ': 'Mexico'}
    home = "America"
    displey(func(home, homeries))
