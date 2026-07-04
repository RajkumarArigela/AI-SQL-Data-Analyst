def validate_sql(sql_query):
    blocked_keywords = ["DROP", "DELETE", "UPDATE", "ALTER"]

    sql_upper = sql_query.upper()

    for keyword in blocked_keywords:
        if keyword in sql_upper:
            return False, f"Blocked unsafe query: {keyword}"

    return True, "Valid SQL"