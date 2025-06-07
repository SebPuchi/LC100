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

questions = {} 

for (root, dirs, files) in os.walk(path):
    
    for file in files:
        if file.endswith(".py"):
            parts = root.split(os.sep)
            print(os.path.join(root, file))
            if len(parts) != 4:
                print("couldn't identify file")
                continue 
            
            # category = parts[2]
            # difficulty = parts[3] if len(parts) > 3 else "unknown"
            # question_file = file
            # question_name = question_file.replace(".py", "").replace("_", " ").title()

            # # Format question display and link
            # relative_path = os.path.join(root, file).replace("\\", "/")
            # link = f"[{question_name}]({relative_path})"
            # row = f"| {link} | True | {category} | `{difficulty}` |"
            # table_rows.append(row)
