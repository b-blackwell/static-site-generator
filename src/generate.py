import os
from pathlib import Path
from markdown_blocks import *

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            header = line.strip("# ").strip()
            return header
    raise ValueError("no header found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")

    with open(from_path, 'r') as file:
        markdown = file.read()
    with open(template_path, 'r') as file:
        template_file = file.read()

    html_node = markdown_to_html_node(markdown)
    html_string = html_node.to_html()

    title = extract_title(markdown)

    template = template_file.replace("{{ Title }}", title).replace("{{ Content }}", html_string).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, 'w') as file:
        file.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path, basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path, basepath)