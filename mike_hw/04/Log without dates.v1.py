# https://www.codewars.com/kata/64cac86333ab6a14f70c6fb6

def check_logs(log):
    # return the minimum number of days
    lst = [int(h) * 3600 + int(m) * 60 + int(s) for h, m, s in [x.split(':') for x in log]]
    days = 1
    if not lst:
        return 0
    prev = lst.pop(0)
    while lst:
        item = lst.pop(0)
        if prev >= item:
            days += 1
        prev = item
    return days


def do_test(a, b, func=check_logs):
    print(f"Test {a}: {['FAIL', 'OK'][func(a) == b]}")


do_test(["12:12:12"], 1)
do_test(["00:00:00", "00:01:11", "02:15:59", "23:59:58", "23:59:59"], 1)
do_test(["12:00:00", "23:59:59", "00:00:00"], 2)
do_test(["12:00:00", "12:00:00", "00:00:00"], 3)
