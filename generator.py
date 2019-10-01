import os
from datetime import datetime
from jinja2 import Environment, PackageLoader
from markdown2 import markdown
import config
import logging
import shutil


def generate_category(category):
    if category not in os.listdir("output"):
        os.makedirs(f"output/{category}")
    posts = read_markdown_files(category)
    create_index(posts, category)
    create_posts(posts, category)


def read_markdown_files(category):
    POSTS = {}
    # Read all markdown files
    for markdown_post in os.listdir(f"content/{category}"):
        file_path = os.path.join(f"content/{category}", markdown_post)

        with open(file_path, "r") as file:
            POSTS[markdown_post] = markdown(file.read(), extras=["metadata"])

    # Returns all posts sorted by date
    return {
        post: POSTS[post] for post in
        sorted(
            POSTS,
            key=lambda post: datetime.strptime(POSTS[post].metadata["date"], "%d-%m-%y"),
            reverse=True
            )
    }


def create_index(posts, category):
    # Loads jinja stuff
    env = Environment(loader=PackageLoader("generator", f"templates/"))
    index_template = env.get_template(f"{category}/index.html")

    posts_metadata = [posts[post].metadata for post in posts]
    tags = [post["tags"] for post in posts_metadata]
    index_html = index_template.render(posts=posts_metadata, tags=tags)

    with open(f"output/{category}/index.html", "w") as file:
        file.write(index_html)


def create_posts(posts, category):
    env = Environment(loader=PackageLoader("generator", f"templates/"))
    post_template = env.get_template(f"{category}/{category}.html")

    for post in posts:
        post_metadata = posts[post].metadata

        post_data = {
            "content": posts[post],
            "title": post_metadata["title"],
            "date": post_metadata["date"]
        }

        post_html = post_template.render(post=post_data)
        post_file_path = f"output/{category}/{post_metadata['slug']}.html"

        os.makedirs(os.path.dirname(post_file_path), exist_ok=True)
        with open(post_file_path, "w") as file:
            file.write(post_html)


def generate_main_pages():
    """
    Generates main pages that rarely or never change
    :return:
    """
    for page in os.listdir("templates/main"):
        env = Environment(loader=PackageLoader("generator", f"templates/"))
        index_template = env.get_template(f"main/{page}")

        # Gets all attributes (such as github url) from config file and puts on `configs` variable
        configs = {item: getattr(config, item) for item in dir(config) if not item.startswith("__")}
        # Renders the html with all config attributes in their places
        index_html = index_template.render(configs)
        # Saves the rendered html
        with open(f"output/{page}", "w") as file:
            file.write(index_html)


def generate_static():
    try:
        shutil.rmtree("output/static")
        logging.info("hello")
    except Exception as e:
        logging.exception(e)
    shutil.copytree("templates/static", "output/static")


if __name__ == "__main__":
    if "output" not in os.listdir("."):
        os.mkdir("output")
    generate_main_pages()
    generate_static()
    for cat in os.listdir("content"):
        generate_category(cat)
