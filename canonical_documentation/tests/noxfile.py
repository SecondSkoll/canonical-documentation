import nox

@nox.session
def vale_lint(session):
    session.install('vale')
    session.run('vale', '--config', '.sphinx/vale.ini')