# https://www.codewars.com/kata/56c2578be8b139bd5c001bd8

def match(job, candidates):
    res = []
    for candidate in candidates:
        if candidate['desires_equity'] and job['equity_max'] > 0 or not candidate['desires_equity']:
            if set(job['locations']) & ({candidate['current_location']} | set(candidate['desired_locations'])):
                res.append(candidate)
    return res


# кусочек проверки с кодварс
candidates = [{
    'desires_equity': True,
    'current_location': 'New York',
    'desired_locations': ['San Francisco', 'Los Angeles']
}, {
    'desires_equity': False,
    'current_location': 'San Francisco',
    'desired_locations': ['Kentucky', 'New Mexico']
}]
job1 = {'equity_max': 0, 'locations': ['Los Angeles', 'New York']}
job2 = {'equity_max': 1.2, 'locations': ['New York', 'Kentucky']}

assert len(match(job1, candidates)) == 0, "не то!"
assert len(match(job2, candidates)) == 2, "не то!"
