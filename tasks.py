from invoke import task


# TODO: Implement unit tests
# @task
# def test(c):
#     """ Runs all unit and integration tests """
#     c.run("green3 .")
# @task
# def cov(c):
#     """ Checks code coverage """
#     c.run(f"coverage run -m py.test {all_tests}")
#     c.run(f"coverage report -m {all_classes}")
#     c.run(f"coverage html {all_classes}")

@task
def run(c):
    """ Runs generator and opens home page """
    c.run("python generator.py")
    html(c)


@task
def html(c):
    """ Opens site home page """
    c.run("python -m webbrowser -t \"output/index.html\"")


@task()
def travis(c):
    """ Runs Travis CI test suite  """
    c.run("flake8 .")
    c.run("jinjalint --parse-only templates")
    c.run("bandit .")
