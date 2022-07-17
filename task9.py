# Необходимо создать два параллельных потока, каждый из которых
# выводил бы на экран числа от 10 до 1 в обратном порядке с интервалом в одну секунду.
# В выводе должно быть понятно какая нить выполняется, и когда каждая из них
# начинает и заканчивает своё выполнение.

import threading, time

def count(i):
    k = 1
    while k < 11:
        print(f'Thread {i}: {k}' + '\n')
        k = k + 1
        time.sleep(1)

for i in range(2):
    th = threading.Thread(target = count, args = (i,))
    th.start()
    #print("Threads active: %i." % threading.active_count())