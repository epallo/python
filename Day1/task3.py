# import os
#
# def     createFolder(directory):
#     try:
#         if not os.path.exists(directory):
#             os.makedirs(directory)
#     except OSError:
#         print('Error: Creating directory. ' + directory)
#
#
# # Example
# createFolder('data', 'data2')
# # Creates a folder in the current directory called data

#Making multiple directories in one location
# import os
# root_path= 'C:/Users/Admin/Desktop/Day1'
# folders = ['2001', '2002', '2003', '2004', '2005']
#
# for folder in folders:
#     os.mkdir(os.path.join(root_path, folder))

#Making a directory within a directory
import os
root_path= 'C:/Users/Admin/Desktop/Day1'
folders = ['1/2/3/4/5']

for folder in folders:
    os.makedirs(os.path.join(root_path, folder))


