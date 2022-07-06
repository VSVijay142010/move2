
from distutils import extension
import os
import shutil
from_dir="C:/Users/mrvsv/Downloads"
to_dir="C:/Users/mrvsv/OneDrive/Documents/img"
list_of_files=os.listdir(from_dir)
print(list_of_files)

for files in list_of_files:
    name,extension=os.path.splitext(files)
    print(name)
    print(extension)
    if extension=='':
      continue
    if extension in['.txt',".doc",'.docx','.pdf']:
      path1=from_dir+'/'+files
      path3=to_dir+'/'+files
      shutil.move(path1,path3)



