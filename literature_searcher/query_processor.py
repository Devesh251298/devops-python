database = {
    "shakespeare": """William Shakespeare (26 April 1564 - 23 April 1616) was an
        English poet, playwright, and actor, widely regarded as the
        greatest writer in the English language and the world's
        pre-eminent dramatist.""",
    "asimov": """Isaac Asimov (2 January 1920 - 6 April 1992) was an
        American writer and professor of Biochemistry, famous for
        his works of hard science fiction and popular science.""",
    "kia":"""Kia Motors Corporation (Korean: 기아자동차; Hanja: 起亞自動車; RR:""",
    "toyota":"""Toyota Motor Corporation (トヨタ自動車株式会社, Toyota Jidōsha Kabushiki-gaisha)""",
    "ford":"""Ford Motor Company is an American multinational automaker headquartered in Dearborn, Michigan, a suburb of Detroit.""",
    "tesla":"""Tesla, Inc. is an American electric vehicle and clean energy company based in Palo Alto, California."""
}


def process(query):
    return [val for key, val in database.items() if key in query.lower()]
