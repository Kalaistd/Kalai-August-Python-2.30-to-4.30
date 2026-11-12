####Multi Threading

#thread

# import _thread as t
# import time
# def a(n):
# 	print("lunch is...", n)
# t.start_new_thread(a, ("dosa",))
# time.sleep(5)
#
#
# import _thread as t
# import time
# def a(n):
#     print("lunch is...",n)
# def b(m):
#     print("dinner is...",m)
# z=t.start_new_thread(a,("dosa",))
# y=t.start_new_thread(b,("Briyani",))
# time.sleep(2)

#
# #Example for threading
#
# import threading as t
# def a(n):
#     print("Lunch is...", n)
# def b(m):
#     print("Dinner is...", m)
# t1 = t.Thread(target=a, args=("dosa",))
# t2 = t.Thread(target=b, args=("Briyani",))
#
# t1.start()
# t2.start()
#
# t1.join()
# t2.join()
#
# print("Completed")
#


# Example
# import threading as t
# def a(name):
#     print(name)
#     print(t.current_thread().name)
#     print(x.is_alive())
#
# x = t.Thread(target=a, args=("Shiva",))
# x.name = "Kalai"
# x.start()
#
# print(x.is_alive())
# print(t.active_count())
# x.join()


#daemon thread

import threading
def a():
    print("I'm function a")
    print(c.daemon)
def b():
    print("I'm function b")
    print(c1.daemon)

c = threading.Thread(target=a, daemon=True)
c.start()
c1 = threading.Thread(target=b, daemon=True)
c1.start()

c.join()
c1.join()

# print(c.daemon)
# print(c1.daemon)




