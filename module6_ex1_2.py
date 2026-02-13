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

th_list1 = []
for i in range(5):
    th_list1.append(Thread(target=get_thread, args=(th_list[i],)))

start_time = time.time()
for i in th_list1:
    i.start()

for i in th_list1:
    i.join()

end_time = time.time()
print("Время выполнения", end_time - start_time)
