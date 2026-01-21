import shutil

total, used, free = shutil.disk_usage("/")
print("Free disk space:", free)
