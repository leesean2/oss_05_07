def convert_p6_to_p3(input_file, output_file):
    with open(input_file, 'rb') as f:
        format_id = f.readline().decode().strip()
        if format_id != 'P6':
            raise ValueError("input file is not a pt ppm file")

        while True:
            line = f.readline().decode().strip()
            if not line.startswith('#'):
                break

        width, height = map(int, line.split())
        maxval = int(f.readline().decode().strip())

        pixels = []
        for i in range(height):
            row = []
            for j in range(width):
                r = int.from_bytes(f.read(1), 'big')
                g = int.from_bytes(f.read(1), 'big')
                b = int.from_bytes(f.read(1), 'big')
                row.append((r, g, b))
            pixels.append(row)

    with open(output_file,'w') as f:
        f.write('P3\n')
        f.write(f'{width} {height}\n')
        f.write(f'{maxval}\n')
        for row in pixels:
            for r, g, b in row:
                f.write(f'{r} {g} {b}\n')


if __name__ == "__main__":
    try:
        convert_p6_to_p3('colorP6File.ppm', 'colorP3File.ppm')
        print("Conversion complete")
    except FileNotFoundError:
        print("Error: File not found")
    except Excetion as e:
        print(f"Error: {str(e)}")
