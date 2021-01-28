import ply.lex as lex

tokens = (
    "STRING",
    "NUMBER",
    "OR",
    "AND",
    "LPAREN",
    "RPAREN",
    "QUOTE",
    "ID",
)

t_OR = r"OR"
t_AND = r"AND"
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_QUOTE = r"\'"
t_ID = r"[a-zA-Z_0-9-][a-zA-Z_0-9-]*"
t_STRING = r"'[a-zA-Z_0-9-]*'"
t_ignore = " \t"


def t_NUMBER(t):
    r"\d+"
    t.value = int(t.value)
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


ID_MAP = {
    "gt": ">",
    "lt": "<",
    "eq": "=",
    "ne": "!=",
    "AND": "AND",
    "OR": "OR",
}


def parse_query(query, columns, query):
    lexer = lex.lex()
    lexer.input(query)
    parsed_query = f"SELECT {columns} FROM ParkingLot"

    if query:
        where_condition = "WHERE"

        while True:
            tok = lexer.token()

            if not tok:
                break

            value, token_type = tok.value, tok.type

            if token_type != "ID":
                where_condition += str(value) + " "
            else:
                where_condition += ID_MAP.get(value, value) + " "
        
        parsed_query += " " + where_condition

    print(parsed_query)
    
    return parsed_query


q = "colour eq 'red'"
print(parse_query(q))
