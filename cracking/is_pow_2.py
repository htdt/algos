def is_pow_2(x):
    return x & (x - 1) == 0


if __name__ == "__main__":
    for i in range(int(1e5)):
        if is_pow_2(i):
            print(i)
