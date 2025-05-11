import os

from markdown_blocks import *

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            header = line.strip("# ").strip()
            return header
    raise ValueError("no header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}...")

    with open(from_path, 'r') as file:
        markdown = file.read()
    with open(template_path, 'r') as file:
        template_file = file.read()

    html_node = markdown_to_html_node(markdown)
    html_string = html_node.to_html()

    title = extract_title(markdown)

    template = template_file.replace("{{ Title }}", title).replace("{{ Content }}", html_string)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, 'w') as file:
        file.write(template)

