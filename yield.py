# coding utf-8

# async/await

def f(x, y):
    if x:
        return 2 * y

f(x,g(a, b, c))


# значние г не будет вычисляться сразу же, а будет вычислено только если x > 0
