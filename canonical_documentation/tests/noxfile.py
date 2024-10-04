import nox

@nox.session
def vale_lint(session):
    session.install('vale')
    session.run('vale', '--help')
    print("This is a placeholder")