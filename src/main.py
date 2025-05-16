from copystatic import *
from generate import *
import sys

def main():
    if not sys.argv[0]:
        basepath = "/"
    else:
        basepath = sys.argv[0]

    print("Deleting public directory...")
    if os.path.exists("public"):
        shutil.rmtree("public")

    print("Copying static files to public directory...")
    copy_directory_contents("static", "public")

    print("Generating content...")
    generate_pages_recursive("content", "template.html", "public", basepath)

if __name__ == "__main__":
    main()
