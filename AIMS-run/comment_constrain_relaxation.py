from pathlib import Path

# Base directory
base_dir = Path(
    "/mnt/c/Users/marce/Documents/BPN/AIMS-run/"
    "ribbons/zigzag/strain/"
)

# Iterate over strain values from 1.0% to 14.0%
for strain in range(1, 15):

    geometry_file = (
        base_dir
        / f"{strain:.1f}%"
        / "input_files_HSE06_inter"
        / "input_files"
        / "geometry.in"
    )

    if not geometry_file.exists():
        print(f"[NOT FOUND] {geometry_file}")
        continue

    # Read original file
    content = geometry_file.read_text()

    # Comment out constrain_relaxation lines
    modified_lines = []
    replacements = 0

    for line in content.splitlines(keepends=True):

        if line.lstrip().startswith("constrain_relaxation .true."):

            indentation = line[:len(line) - len(line.lstrip())]

            modified_line = (
                indentation
                + "# "
                + line.lstrip()
            )

            modified_lines.append(modified_line)
            replacements += 1

        else:
            modified_lines.append(line)

    # Save modifications
    if replacements > 0:

        geometry_file.write_text("".join(modified_lines))

        print(
            f"[MODIFIED] {strain:.1f}% "
            f"({replacements} replacements)"
        )

    else:
        print(f"[UNCHANGED] {strain:.1f}%")
