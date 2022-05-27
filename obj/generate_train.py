import os

img_files = []
os.chdir(os.path.join("data", "obj"))
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".png"):
        img_files.append("data/obj/" + filename)

os.chdir("..")

with open("train.txt", "w") as outfile:
    for img in img_files:
        outfile.write(img)
        outfile.write("\n")
    outfile.close()
os.chdir("..")