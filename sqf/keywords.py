class Keyword:
    def __init__(self, token):
        self._token = token

    @property
    def value(self):
        return self._token

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._token == other._token
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return self._token

    def __repr__(self):
        return 'R<%s>' % self._token

    def __hash__(self):
        return hash(self._token)


KEYWORDS = {
    'if', 'then', 'else', 'do', 'while', 'for', 'to', 'from', 'step', 'foreach',
    '(', ')', '[', ']', '{', '}',
    ',', ':', ';', 'nil',
    'case', 'switch', 'default',
    'private',
    '=', '+', '-', '*', '/', '%', 'mod', '^', 'max', 'floor',
    'setVariable', 'getVariable',
    'set', 'in', 'select', 'find', 'append', 'pushBack', 'pushBackUnique', 'reverse',
    'call', 'spawn', 'SPAWN',
    '&&', 'and', '||', 'or',
    'isEqualTo', '==', '!=', '>', '<', '>=', '<=', '!', 'not',
    'isNull', 'isNil',
    'units', 'count',
    'createMarker', 'getmarkerpos',
    'publicVariable', 'publicVariableServer', 'publicVariableClient',
    'addPublicVariableEventHandler', 'isServer', 'isClient', 'isDedicated',
}


class Namespace(Keyword):
    pass


NAMESPACES = [Namespace('missionNamespace'), Namespace('profileNamespace'), Namespace('uiNamespace'),
              Namespace('parsingNamespace')]

KEYWORDS = set(Keyword(s) for s in KEYWORDS)
KEYWORDS = KEYWORDS.union(NAMESPACES)

KEYWORDS_MAPPING = dict()
for keyword in KEYWORDS:
    KEYWORDS_MAPPING[keyword.value] = keyword

# operators by precedence
ORDERED_OPERATORS = [Keyword(s) for s in ('private', '=', 'count', '>', 'units', 'SPAWN', 'spawn', '&&', '!',
                                          'getVariable')]
