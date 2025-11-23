# Write a program to convert user given bytes into KB, MB, GB

bytes = input("Enter Bytes : ")
bytes = int(bytes)
kb = bytes/1024
mb = bytes/(1024*1024)
gb = bytes/(1024*1024*1024)
print(f"Bytes = {bytes} KB = {kb} MB = {mb} GB = {gb}")