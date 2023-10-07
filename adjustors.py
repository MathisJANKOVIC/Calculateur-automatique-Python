def adjust_type(value: str) -> int | float :
    """Converts a string number to an integer or float based on its format."""
    if("." in value):
        return float(value)
    else:
        return int(value)

def adjust_sign(coef) -> str :
    """ Adjusts the sign of the coefficient or the single-sign for display in the context of a no first therm in an equation."""
    if(type(coef) is int or type(coef) is float):
        if(coef > 0):
            return f"+ {coef}"
        if(coef == 0):
            return ""
        if(coef < 0):
            return f"- {-coef}"
    else:
        if(coef == ""):
            return "+ "
        if(coef == "-"):
            return "- "

def adjustx(coef: int):
    """ Adjusts the coefficient for display in the context of an 'x' term in an equation."""
    if(coef == 1):
        return ""
    elif(coef == -1):
        return "-"
    else:
        return coef
