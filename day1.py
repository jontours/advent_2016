import numpy as np
positions = 'L4, L3, R1, L4, R2, R2, L1, L2, R1, R1, L3, R5, L2, R5, L4, L3, R2, R2, L5, L1, R4, L1, R3, L3, R5, R2, L5, R2, R1, R1, L5, R1, L3, L2, L5, R4, R4, L2, L1, L1, R1, R1, L185, R4, L1, L1, R5, R1, L1, L3, L2, L1, R2, R2, R2, L1, L1, R4, R5, R53, L1, R1, R78, R3, R4, L1, R5, L1, L4, R3, R3, L3, L3, R191, R4, R1, L4, L1, R3, L1, L2, R3, R2, R4, R5, R5, L3, L5, R2, R3, L1, L1, L3, R1, R4, R1, R3, R4, R4, R4, R5, R2, L5, R1, R2, R5, L3, L4, R1, L5, R1, L4, L3, R5, R5, L3, L4, L4, R2, R2, L5, R3, R1, R2, R5, L5, L3, R4, L5, R5, L3, R1, L1, R4, R4, L3, R2, R5, R1, R2, L1, R4, R1, L3, L3, L5, R2, R5, L1, L4, R3, R3, L3, R2, L5, R1, R3, L3, R2, L1, R4, R3, L4, R5, L2, L2, R5, R1, R2, L4, L4, L5, R3, L4'
#positions = 'R8, R4, R4, R8'
bearing = 0
quadrant = []
multipliers = np.array([[0,1], [-1,0], [0,-1], [1, 0]])
directions = {0:1, 1:-1, 2:-1, 3:1}
turns = {'R': 1, 'L': -1}
distance = np.array([0,0])
visited = {'0': [0]}
traveled_positions = []
position = np.array([0,0])
traveled_positions.append(np.copy(position))
allPositions = []
exacts = {(x,y) for x in range(0,-8,-1) for y in range(3,4)}
#print(exacts)
indexer = 0
history = {}
dups = {}

for direction in positions.split():

	direction = direction.strip(',')
	bearing = (bearing + int(turns[direction[0]])) % 4
	distance += multipliers[bearing] * int(direction[1:])
	position += ((int(direction[1:])) * multipliers[bearing])
	traveled_positions.append(np.copy(position))
	oldPosition = traveled_positions[len(traveled_positions) - 2]
	#print(directions[bearing])
	#print(bearing)
	allPositions.append({(x,y) for x in range(oldPosition[0], position[0] + (directions[bearing]), directions[bearing]) for y in range(oldPosition[1], position[1] + (directions[bearing]), directions[bearing]) })
	temp_pos = [(x,y) for x in range(oldPosition[0], position[0] + (directions[bearing]), directions[bearing]) for y in range(oldPosition[1], position[1] + (directions[bearing]), directions[bearing])]
	#print(temp_pos)
	for pos in temp_pos[1:]:
		if history.get(pos[0]):
			if pos[1] in history[pos[0]]:
				print('dup found!!')
				print(pos)
				print('dup distance ' + str(abs(pos[0]) + abs(pos[1])))
				dups[str(pos)] = abs(pos[0]) + abs(pos[1])
			history[pos[0]].append(pos[1])
		else:
			history[pos[0]] = [pos[1]]
	#print(history)
	#print(allPositions)
	

final_distance = abs(distance[0]) + abs(distance[1])
print("final distance: " + str(final_distance))
#print(traveled_positions)
print(dups)