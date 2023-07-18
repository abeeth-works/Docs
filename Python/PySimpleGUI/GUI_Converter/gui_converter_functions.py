# all conversions done here
def km_to_m(km):
    km = float(km)
    return f"{km}Km is {round(km * 0.6214)}miles (rounded)"

def kg_to_p(kg):
    kg = float(kg)
    return f"{kg}Kg is {round(kg * 2.2046)}pounds (rounded)"

def sec_to_min(sec):
    sec = float(sec)
    return f"{sec}seconds is {sec / 60} minutes"