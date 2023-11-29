import Detective


def g_variables(name):
    global victory
    global detective

    detective = Detective.Detective(name)

    victory = False
