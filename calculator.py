# 65070503410 Charunthon Limseelo - Calculator Testing
# Submit to Aj. Chaiyong Ragkhitwetsagul
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        negative = False
        if(b < 0):
            negative = True
            b = -b
        for i in range(b):
            result = self.add(result, a)
        if negative:
            result = -result
        return result


    def divide(self, a, b):
        negative = False
        if b == 0:
            print ("Undefined")
        result = 0
        if a < 0:
            a = -a
            negative = True
        if b < 0:
            b = -b
            negative = True
        while a >= b:
            a = self.subtract(a, b)
            result += 1
        if negative:
            result = result
        return result

    def modulo(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Modulo by zero is undefined")
        abs_a = a
        if abs_a < 0:
            abs_a = -abs_a
        abs_b = b
        if abs_b < 0:
            abs_b = -abs_b

        result = abs_a
        while result >= abs_b:
            result = result - abs_b

        if a < 0 and b < 0:
            return -result

        if a < 0 and b > 0:
            if result != 0:
                return b - result
            return 0
        

        if a > 0 and b < 0:
            if result != 0:
                return b + result
            return 0
        
        return result

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(5, 2))
    print("Example: multiplication: ", calc.multiply(3, 7))
    print("Example: division: ", calc.divide(5, 2))
    print("Example: modulo: ", calc.modulo(5, 2))