from copystatic import *

def main():
    print("Deleting public directory...")
    if os.path.exists("public"):
        shutil.rmtree("public")

    print("Copying static files to public directory...")
    copy_directory_contents("static", "public")

if __name__ == "__main__":
    main()
