# https://www.codewars.com/kata/64cac86333ab6a14f70c6fb6

def check_logs(log):
    lst = [x.split(':') for x in log]
    res = []
    for item in lst:
        res.append(int(item[0]) * 3600 + int(item[1]) * 60 + int(item[2]))

    day = 1
    for i in range(len(res) - 1):
        if res[i] >= res[i + 1]:
            day += 1

    return 0 if not log else day


def do_test(a, b, func=check_logs):
    print(f"Test {a}: {['FAIL', 'OK'][func(a) == b]}")


do_test(["12:12:12"], 1)
do_test(["00:00:00", "00:01:11", "02:15:59", "23:59:58", "23:59:59"], 1)
do_test(["12:00:00", "23:59:59", "00:00:00"], 2)
do_test(["12:00:00", "12:00:00", "00:00:00"], 3)
