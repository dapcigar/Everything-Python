def calculate_volume(radius, lenght, pi=3.145):
    result = (radius ** 2) * lenght * round(pi, 2)

    return result


res = calculate_volume(5, 17)
print(res)


# Kwags and Args

def info(*args, **kwargs):
    print(args, kwargs)


info(1, 2, 3, 4, 5, name="Ola", age=22, location="Lagos")
