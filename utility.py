PRINTING_TIME = 0.25

def is_decimal(value):
    if(value.replace(".","").replace("-","").isdecimal()):
        return True
    else:
        return False

def adjust_type(value):
    if("." in value):
        return float(value)
    else:
        return int(value)

def adjust_sign(coef):
    if(type(coef) == int or type(coef) == float):
        if(coef > 0):
            return (f"+ {coef}")
        if(coef == 0):
            return ("")
        if(coef < 0):
            return (f"- {-coef}")
    else:
        if(coef == ""):
            return ("+ ")
        if(coef == "-"):
            return ("- ")

def adjust_x(coef):
    if(coef == 1):
        return ("")
    elif(coef == -1):
        return ("-")
    else:
        return (coef)
