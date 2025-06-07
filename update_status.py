import subprocess
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import july
from july.utils import date_range

# runs git as subprocess -- collects all the logged dates committed in dir 
def get_commit_dates(path, since, until):
    git_log_cmd = [
        "git", "log",
        "--since", since,
        "--until", until,
        "--pretty=format:%ad", "--date=short",
        "--", path
    ]
    
    result = subprocess.run(git_log_cmd, capture_output=True, text=True)
    dates = result.stdout.strip().split('\n')
    return set(dates)

mpl.rcParams['font.family'] = 'Hack Nerd Font Mono'
dates = date_range("2025-05-01", "2025-8-31")
# May need to update last date in the future
commit_dates = get_commit_dates("./questions/", "2025-05-01", "2025-08-31")
print("Commit dates found:", commit_dates)

# maps matches to 1 to graph
data = np.array([1 if d.strftime("%Y-%m-%d") in commit_dates else 0 for d in dates])

fig, ax = plt.subplots(nrows=1, ncols=4, figsize=(12, 3.5))

july.month_plot(dates, data, month=5, ax=ax[0])
july.month_plot(dates, data, month=6, ax=ax[1])
july.month_plot(dates, data, month=7, ax=ax[2])
july.month_plot(dates, data, month=8, ax=ax[3])

fig.suptitle("Completed Days", fontsize=16)
#plt.savefig("./auto_assets/plot.png", dpi=300, bbox_inches='tight')

# Walk question dir  
path = "./questions"


markdown_rows = []

for (root, dirs, files) in os.walk(path):
    row = ""
    for file in files:
        if file.endswith(".py"):
            file_path = os.path.join(root, file)
            parts = root.split(os.sep)
            if len(parts) != 4:
                print("couldn't identify file")
                continue 
            #adds link thing in markdown
            row +="| [" +file[:-3] +"](" + file_path +") | " + parts[2] + " | " + parts[3] + " |\n"

            markdown_rows.append(row)



# Writing to file
start_index = None

with open("./README.md", "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if "# TABLE ROW START" in line:
        start_index = i
        break

if start_index is not None:
    new_lines = lines[:start_index + 1] + markdown_rows

    with open("./README.md", "w") as f:
        f.writelines(new_lines)
    print("README.md updated successfully.")
else:
    print("Marker '# TABLE ROW START' not found in README.md.")

