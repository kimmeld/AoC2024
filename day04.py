class Puzzle:
    """
    Helper class to make working with a puzzle a little easier
    """
    puzzle = []
    width = 0
    height = 0

    def __init__(self, puzzle_array) -> None:
        self.puzzle = puzzle_array
        for row in self.puzzle:
            self.width = max(self.width, len(row))
        self.height = len(self.puzzle)

    def get(self, w, h):
        """
        Get the cell in a puzzle, returning a ' ' for an out-of-bounds cell
        """
        if w < 0 or h < 0 or w > (self.width-1) or h > (self.height-1):
            ret = ' '
        else:
            ret = self.puzzle[h][w]        
        return ret

# Read input
inputpuzzle = []
with open("day04.input") as f:
    for l in f.readlines():
        line = [c for c in l][0:-1]
        inputpuzzle.append(line)
puzzle = Puzzle(inputpuzzle)

# For part 1
def check_xmas(puzzle, w, h, ww, hh):
    """
    See if we have an XMAS at (w,h), incrementing the location by (ww,hh)
    """
    search = "XMAS"
    for c in range(len(search)):
        if puzzle.get(w + (c*ww), h + (c*hh)) != search[c]:
            return False
    return True

def check_x_mas(puzzle, w, h):
    """
    See if we have an X-MAS centered on (w,h)
    """
    # Always has an 'A' in the middle
    if puzzle.get(w,h) == 'A':
        # Get surrounding corners
        ul = puzzle.get(w-1,h-1)
        ur = puzzle.get(w+1,h-1)
        ll = puzzle.get(w-1,h+1)
        lr = puzzle.get(w+1,h+1)

        # See if the corners are correct to form an X-MAS
        if ((ul == "M" and lr == "S") or (ul == "S" and lr == "M")) and ((ur == "M" and ll == "S") or (ur == "S" and ll == "M")):
            return True
        
        return False

num_xmas = 0
num_x_mas = 0
for h in range(0, puzzle.height+1):
    for w in range(0, puzzle.width+1):
        if check_xmas(puzzle, w, h, 1, 1):
            num_xmas += 1 
        if check_xmas(puzzle, w, h, -1, 1):
            num_xmas += 1 
        if check_xmas(puzzle, w, h, 1, -1):
            num_xmas += 1 
        if check_xmas(puzzle, w, h, -1, -1):
            num_xmas += 1 
        if check_xmas(puzzle, w, h, 1, 0):
            num_xmas += 1 
        if check_xmas(puzzle, w, h, 0, 1):
            num_xmas += 1 
        if check_xmas(puzzle, w, h, -1, 0):
            num_xmas += 1 
        if check_xmas(puzzle, w, h, 0, -1):
            num_xmas += 1 
        if h == 1 and w == 2:
            print("break")
        if check_x_mas(puzzle, w, h):
            num_x_mas += 1
print(f"Part 1 = {num_xmas}")
print(f"Part 2 = {num_x_mas}")