import shutil

shutil.copy("walrus.py", "copied.py")
shutil.copy2("walrus.py", "copied2.py")
shutil.copytree("../day_32", "copied_dir")
# shutil.move("../day_32", "../day_31")
# shutil.rmtree("copied_dir")
