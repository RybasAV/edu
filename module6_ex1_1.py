import time
from threading import Thread


def counter():
    pass


def get_thread(thread_name):
    time.sleep(1)
    print(thread_name.name)


th_list = []
for i in range(1, 6):
    th_list.append(Thread(target=counter, args=(7,), name=f"Поток №{i}"))

for i in range(5):
    if i == 0:
        start_time = time.time()
    get_thread(th_list[i])

end_time = time.time()
print("Время выполнения", end_time - start_time)
