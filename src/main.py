from copystatic import *
from generate import *
import sys

def main():
    if len(sys.argv) == 1:
        basepath = "/"
    else:
        basepath = sys.argv[1]

    print("Deleting public directory...")
    if os.path.exists("docs"):
        shutil.rmtree("docs")

    print("Copying static files to public directory...")
    copy_directory_contents("static", "docs")

    print("Generating content...")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()
