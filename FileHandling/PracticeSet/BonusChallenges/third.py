import os
from pathlib import Path
import sys

get_loc = Path(__file__).parent / "task2.txt"
# # print(get_loc)
# if len(sys.argv) < 2:
#     print("Please provide folder name")
#     sys.exit()

# folder = sys.argv[1]
# total_size = 0

# for file in os.listdir(folder):
#     file_path = os.path.join(file,folder)

# if os.path.isfile(file_path):
#         total_size += os.path.getsize(get_loc)

# print("Total size:", total_size, "bytes")

import os
import sys

folder = sys.argv[1]

total_size = 0

# for file in os.listdir(folder):
#     file_path = os.path.join(folder, file)

if os.path.isfile(get_loc):
    total_size += os.path.getsize(get_loc)

print("Total size:", total_size, "bytes")




# os.path.getsize(get_loc)