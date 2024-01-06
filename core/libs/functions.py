from django.db.models import Func

class Levenshtein(Func):
    # template = "%(function)s(%(expressions)s, '%(search_term)s')"
    template = "%(function)s(CAST(%(expressions)s AS text), CAST('%(search_term)s' AS text))"
    function = "levenshtein"

    def __init__(self, expression, search_term, **extras):
        super(Levenshtein, self).__init__(
            expression,
            search_term=search_term,
            **extras
        )