'''
this is so bad
explorer has 2 sets of coordinates, a(x,y) and b(x,y)
a is the location coordinates, b is the direction it is facing ie the square immediately in front of it
the explorer begins with 3 inputs: t, i, m
t (1<=t<=100) is number of moves for trail to disappear
i (1<=len(i)<=10) upper case, indicating explorer's instructions
m (1<=m<=10000), how many moves explorer makes

unable to make moves, stop permanently
must print explorer coordinates after making moves

again referring to a solution to help
https://github.com/matthewelse/british-informatics-olympiad/blob/master/2019/q2.py

he used a rotational thing which is quite smart actually.


'''

a = [0,0] # declare location
b = [0,1] # declare direction


def recv():
	while True:
		try:
			t, i, m = input().split()
			t = int(t)
			if not 1<=t<=100:
				print("enter valid decay length")
				continue
			if not 1<=len(i)<=10:
				print("enter valid number of instructions")
				continue
			m = int(m)
			if not 1<=m<=10000:
				print("enter valid number of moves")
			break
		except ValueError:
			print("please input proper data types (integer, string, integer)")
	return t, i, m


def turn():
	



def main():
	t, i, m = recv()


if __name__ = '__main__':
	main()
