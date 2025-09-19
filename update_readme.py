import os

# Walk question dir  
path = "./questions"

markdown_rows = []
header ="| Question | Category | Difficulty |\n"
formatting = "|:-----------------------------|:---------|:------------|\n"
markdown_rows.append(header)
markdown_rows.append(formatting)

for (root, dirs, files) in os.walk(path):
    for file in files:
        row = ""
        if file.endswith(".py"):
            print(file)
            file_path = os.path.join(root, file)
            parts = root.split(os.sep)
            if len(parts) != 4:
                print("***", parts)
                print("couldn't identify file")
                continue 
            #adds link thing in markdown
            row +="| [" +file[:-3] +"](" + file_path +") | " + parts[2] + " | `" + parts[3] + "` |\n"

            markdown_rows.append(row)


# Writing to file
start_index = None

with open("./README.md", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "## Completed Questions" in line:
        start_index = i
        break

if start_index is not None:
    new_lines = lines[:start_index + 1] + markdown_rows

    with open("./README.md", "w") as f:
        f.writelines(new_lines)
    print("README.md updated successfully.")
else:
    print("Marker '# TABLE ROW START' not found in README.md.")

