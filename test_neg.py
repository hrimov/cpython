# help(neg)

print(neg(123))
print(neg(-123))

print(neg(456))
print(neg(-456))


class Number:
    def __init__(self, value: int):
        self.value = value

    def __neg__(self):
        return -2 * self.value


num = Number(10)
print(neg(num))





