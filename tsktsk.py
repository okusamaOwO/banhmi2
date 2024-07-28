print("duma cay the nhi")
import shutil
import os

src_dir = r"C:\Users\lanhu\OneDrive\Hình ảnh"
des_dir = r"C:\Users\lanhu\PycharmProjects\GitPractice"
if os.path.exists(des_dir) and os.path.isdir(src_dir):
    for file in os.listdir(src_dir):
        if file.lower().endswith((".png", ".jpg", ".jpeg")):
            shutil.copyfile(os.path.join(src_dir, file), os.path.join(des_dir, file))
