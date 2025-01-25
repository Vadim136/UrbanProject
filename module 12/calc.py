import logging

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    try:
        a / b
        logging.info(f"Succesful divide {a} / {b}")
        return a / b
    except ZeroDivisionError as err:
        logging.error("Na nol' ne deli!!!", exc_info=True)
        return 0
        

def sqrt(a):
    return a**0.5

def pow(a,b):
    return a**b

# def add(a, b):
#     return a**2 + b**2

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filemode="w", filename="calc.log",
                        format="%(asctime)s | %(levelname)s | %(message)s")
    
    
    print(div( 3, 4))
    print(div( 3, 0))