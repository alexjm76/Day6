def test(func):
	def new_func(*args, **kwargs):
		print("start")
		result = func(*args, **kwargs)
		print("Result:", result)
		print("end")
		return result
	return new_func


@test
def add(a, b):
	return a + b

add(2, 4)