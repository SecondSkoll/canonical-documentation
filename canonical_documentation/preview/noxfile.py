import nox

@nox.session
def preview(session):
    session.install('sphinx-autobuild', 'canonical-sphinx', 'sphinxcontrib-svg2pdfconverter')

    if session.posargs:
        dir = session.posargs[0]
    else:
        dir = '.'

    session.run('sphinx-autobuild', dir, '.build/html')