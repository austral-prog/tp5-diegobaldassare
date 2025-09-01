# Replace the "ANSWER HERE" for your answer

def number_to_month(month):
    # return "ANSWER HERE" # Remove this line and implement
    """Given a number between 1 and 12, return the corresponding month name as a string.
    If the number is not between 1 and 12, return "error".
    """
    months = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
    if 1 <= month <= 12:
        return months[month - 1]
    return "error"