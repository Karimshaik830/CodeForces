import sys


def solve():
    # Read all inputs at once and split by whitespace
    input_data = sys.stdin.read().split()

    if not input_data:
        return

    n = int(input_data[0])

    # Create a dictionary mapping the shape name to its face count
    faces_map = {
        "Tetrahedron": 4,
        "Cube": 6,
        "Octahedron": 8,
        "Dodecahedron": 12,
        "Icosahedron": 20
    }

    total_faces = 0

    # Loop through the shapes and add up the faces
    for i in range(1, n + 1):
        shape = input_data[i]
        total_faces += faces_map[shape]

    # Print the final result
    print(total_faces)


if __name__ == '__main__':
    solve()