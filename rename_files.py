import os

def rename_files():
	file_list = os.listdir(r"C:\test2\to999\")
	saved_path = os.getcwd()
	os.chdir(r"C:\test2\to999\")

	for file_name in file_list:
		a = file_name[19:22]
		os.rename(file_name, file_name[:17]+"@0"+a)

rename_files()