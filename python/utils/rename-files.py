import os
from re import sub
import fnmatch

# walk through the folder
f = open("./101_ObjectCategories/101_ObjectCategories.txt", "w")
for root, dirs, files in os.walk('101_ObjectCategories'):
    for str_each_folder in dirs:
        # we get the directory path
        str_the_path = '/'.join([root, str_each_folder])

        files_number = len(fnmatch.filter(os.listdir(str_the_path), '*.jpg'))
        # list all the files using directory path
        for str_each_file in os.listdir(str_the_path):
            # look for the files we want
            if str_each_file.endswith('.jpg'):
                # now add the new one
                str_new_name = str_each_folder + '_' + str_each_file
                # full path for both files
                str_old_name = '/'.join([str_the_path, str_each_file])
                str_new_name = '/'.join([root, str_new_name])

                # now rename using the two above strings
                # and the full path to the files
                os.rename(str_old_name, str_new_name)

        # we can print the folder name so we know
        # that all files in the folder are done
        print '%s, %d images' % (str_each_folder, files_number)
        f.writelines('%s, %d images\n' % (str_each_folder, files_number))

f.close