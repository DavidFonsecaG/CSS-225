import Detective


def g_variables():
    global victory
    global detective

    d_name = "Alex Mercer"
    d_town = "Raven's Hollow"
    d_objective = ("\nYour objective is to solve the mysterious murder of Mayor Richard\n"
                   "Thornton. As you explore the secrets of Raven's Hollow, you must gather clues, interrogate\n"
                   "suspects, and navigate a web of lies to uncover the truth.")
    d_description = ("a seasoned investigator known for your sharp instincts\n"
                     "and relentless pursuit of justice."
                     "Recently transferred to the quiet town of Raven's Hollow,\n"
                     "you're about to face a case that\n"
                     "will challenge your skills and intuition like never before")

    detective = Detective.Detective(d_name, d_town, d_description, d_objective)

    victory = False
