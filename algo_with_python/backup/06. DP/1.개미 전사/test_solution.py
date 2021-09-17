import solution as sol


def test():
	assert sol.solution([4, 3, 1]) == 5
	assert sol.solution([1, 3, 1]) == 3
	assert sol.solution([1, 3, 1, 5]) == 8
	assert sol.solution([4, 3, 2, 1, 9]) == 15

