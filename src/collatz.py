import matplotlib.pyplot as plot

def collatz(num):
    con = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        con += 1
    return con

x = list(range(1, 10001))
y = [collatz(n) for n in x]

plot.figure(figsize=(10, 6))
plot.scatter(x, y, s=1)
plot.title('Número de iteraciones de la conjetura de Collatz para números del 1 al 10000')
plot.xlabel('Número inicial (n)')
plot.ylabel('Número de iteraciones hasta converger a 1')
plot.show()