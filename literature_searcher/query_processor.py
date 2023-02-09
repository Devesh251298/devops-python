database = {
    "shakespeare": """William Shakespeare (26 April 1564 - 23 April 1616) was an
        English poet, playwright, and actor, widely regarded as the
        greatest writer in the English language and the world's
        pre-eminent dramatist.""",
    "asimov": """Isaac Asimov (2 January 1920 - 6 April 1992) was an
        American writer and professor of Biochemistry, famous for
        his works of hard science fiction and popular science.""",
    "ford":"""Ford Motor Company is an American multinational automaker headquartered in Dearborn, Michigan, a suburb of Detroit.""",
    "tesla":"""Tesla, Inc. is an American electric vehicle and clean energy company based in Palo Alto, California.""",
    "kant" : """"Immanuel Kant was a German philosopher who is considered a central figure in modern philosophy.""",
    "kia":"""Kia Motors Corporation, commonly known as Kia, is a South Korean multinational automotive manufacturer headquartered in Seoul."""
}


def process(query):
    return [val for key, val in database.items() if key in query.lower()]
