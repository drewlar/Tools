def split(D, N):
	'''
	Prints how many amoebas there are up to N iterations in a D dimensional grid.
		Andrew's Amoeba Problem:
			Consider a D-dimensional grid of points. A amoeba in cube X = (x_1, x_2, x_3, x_4, ..., x_D)
			can divide itself into D amoeba(s) to occupy points (x_1 + 1, x_2, ..., x_D), 
			(x_1, x_2 + 1, x_3, ..., x_D), ..., (x_1, x_2, ..., x_D +1); provided these cubes are empty
			and exactly only 1 amoeba splits into these points (i.e. if >1 amoebas split into the same point
			no amoeba can grow there). In addition, an amoeba dies after splitting.

			Orginally there is only one amoeba on the point O = (0, 0, 0, ..., 0), where O is within R^D.
			Let S_D(N) be the number of amoebas in a D-dimensional grid after N division.

			For example, S_3(1) = 3, S_3(2) = 3.

			Find S_D(1000).

			What about S_D(1020)?

	Paramaters:
		D: dimensional grid for amoeba; int: >0
		N, Number of splits to compute; int >=1
	'''
	# Checking parameters are within bounds
	assert isinstance(D,int), 'Input "D" is not an int'
	assert isinstance(N,int), 'Input "N" is not an int'
	assert D > 0, 'Input "D" is not positive'
	assert N >= 1, 'Input "N" is not poistive'

	# Intializeing values:
	deadspace = set()		# Will help us keep track of space where >1 amoebas grow
	cur_alivespace = [tuple((0 for i in range(D)))]
	new_alivespace = []
	
	print("==== 0 to 3 ====\n")
	print(len(cur_alivespace),end=" ")

	for split in range(1,N+1):
		for amoeba in cur_alivespace:
			# Find the children of an amoeba and insert into our living space
			# if a child already exist (i.e. point is occupied):
			#	black list point
			# no amoeba can grow on blacklisted points
			children = tuple(shift_1(amoeba, dim)
							 for dim in range(len(amoeba)))

			for child in children:
				if child in new_alivespace:
					new_alivespace.remove(child)
					deadspace.add(child)
				if child not in deadspace:
					new_alivespace.append(child)
		# Reset containers
		cur_alivespace = new_alivespace.copy()
		new_alivespace.clear()
		deadspace.clear()

		print(len(cur_alivespace),end=" ")
		if (split) % 4 == 3 and not split == N:
			print("\n\n==== ", split+1, "to", split+4, "====\n")
	print()

# Helper function to add 1 to a given point at  given x_index
def shift_1(tup, index=0):
	return tuple((tup[i] + 1 
			   	if i == index 
				else tup[i] 
				for i in range(len(tup))))



split(3,14)
