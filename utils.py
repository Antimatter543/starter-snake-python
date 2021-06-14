def offBoard(board, entity_pos):
	"""
	Returns True if the entity position is out of bounds
	"""
	if (entity_pos[0] < 0 or entity_pos[0] >= board['width']) or entity_pos[1] < 0 or entity_pos[1] >= board['height']: # Checks if either the x/y is over the board state range.
			return True
	return False # If it makes it here we are ok.

def move_to_coord(direction, head):
	# Returns the coordinates that the head will be at if it moves the given direction.
	if direction=='up':
		return (head[0], head[1]+1)

	if direction=='down':
		return (head[0], head[1]-1)

	if direction=='left':
		return (head[0]-1, head[1])
	if direction=='right':
		return (head[0]+1, head[1])

def equal_coords(a, b) -> bool:
	""" Checks if coords are equal"""
	return a[0] == b[0] and a[1]==b[1]
