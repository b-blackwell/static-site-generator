from copystatic import *
from generate import *

def main():
    print("Deleting public directory...")
    if os.path.exists("public"):
        shutil.rmtree("public")

    print("Copying static files to public directory...")
    copy_directory_contents("static", "public")

    print("Generating content...")
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()
