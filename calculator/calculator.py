import math
import cmath
import statistics
import re
from typing import Union, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum
import numpy as np
from fractions import Fraction
from decimal import Decimal, getcontext

# Set decimal precision
getcontext().prec = 50

class CalculatorMode(Enum):
    BASIC = "Basic"
    SCIENTIFIC = "Scientific"
    PROGRAMMER = "Programmer"
    STATISTICS = "Statistics"
    MATRIX = "Matrix"

@dataclass
class CalculationHistory:
    expression: str
    result: Union[float, complex, str]
    mode: str
    timestamp: str

class AdvancedCalculator:
    def __init__(self):
        self.memory = 0
        self.history = []
        self.variables = {}
        self.last_result = 0
        self.angle_mode = 'deg'
        
        # Math constants
        self.constants = {
            'pi': math.pi,
            'e': math.e,
            'tau': math.tau,
            'phi': (1 + math.sqrt(5)) / 2,
            'euler': 0.5772156649015329,
            'c': 299792458,
            'g': 9.80665,
            'h': 6.62607015e-34,
            'na': 6.02214076e23,
        }
    
    # Basic math
    def add(self, x, y):
        return x + y
    
    def subtract(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y
    
    def divide(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        return x / y
    
    def modulo(self, x, y):
        return x % y
    
    def integer_divide(self, x, y):
        if y == 0:
            return "Error: Division by zero"
        return int(x // y)
    
    # Powers and roots
    def power(self, base, exponent):
        return base ** exponent
    
    def sqrt(self, x):
        if x < 0:
            return cmath.sqrt(x)
        return math.sqrt(x)
    
    def nth_root(self, x, n):
        if x < 0 and n % 2 == 0:
            return complex(x) ** (1/n)
        return x ** (1/n)
    
    def cube_root(self, x):
        return np.cbrt(x)
    
    # Exponential and logarithm
    def exp(self, x):
        return math.exp(x)
    
    def ln(self, x):
        if x <= 0:
            return "Error: ln undefined for non-positive values"
        return math.log(x)
    
    def log10(self, x):
        if x <= 0:
            return "Error: log undefined for non-positive values"
        return math.log10(x)
    
    def log2(self, x):
        if x <= 0:
            return "Error: log undefined for non-positive values"
        return math.log2(x)
    
    def log_base(self, x, base):
        if x <= 0 or base <= 0 or base == 1:
            return "Error: Invalid logarithm parameters"
        return math.log(x, base)
    
    # Trigonometry
    def _convert_angle(self, angle, to_radians=True):
        if self.angle_mode == 'deg':
            return math.radians(angle) if to_radians else angle
        elif self.angle_mode == 'grad':
            return (angle * math.pi / 200) if to_radians else angle
        return angle
    
    def sin(self, x):
        return math.sin(self._convert_angle(x))
    
    def cos(self, x):
        return math.cos(self._convert_angle(x))
    
    def tan(self, x):
        return math.tan(self._convert_angle(x))
    
    def asin(self, x):
        if -1 <= x <= 1:
            result = math.asin(x)
            return self._convert_angle(result, False) if self.angle_mode != 'rad' else result
        return "Error: asin domain error"
    
    def acos(self, x):
        if -1 <= x <= 1:
            result = math.acos(x)
            return self._convert_angle(result, False) if self.angle_mode != 'rad' else result
        return "Error: acos domain error"
    
    def atan(self, x):
        result = math.atan(x)
        return self._convert_angle(result, False) if self.angle_mode != 'rad' else result
    
    def sinh(self, x):
        return math.sinh(x)
    
    def cosh(self, x):
        return math.cosh(x)
    
    def tanh(self, x):
        return math.tanh(x)
    
    # Special functions
    def factorial(self, n):
        if n < 0:
            return "Error: Factorial undefined for negative numbers"
        if n > 170:
            return "Error: Number too large"
        return math.factorial(int(n))
    
    def gamma(self, x):
        return math.gamma(x)
    
    def beta(self, x, y):
        return math.gamma(x) * math.gamma(y) / math.gamma(x + y)
    
    def erf(self, x):
        return math.erf(x)
    
    def combination(self, n, r):
        if r > n or r < 0:
            return 0
        return math.comb(int(n), int(r))
    
    def permutation(self, n, r):
        if r > n or r < 0:
            return 0
        return math.perm(int(n), int(r))
    
    def gcd(self, a, b):
        return math.gcd(int(a), int(b))
    
    def lcm(self, a, b):
        return abs(int(a) * int(b)) // math.gcd(int(a), int(b))
    
    # Complex numbers
    def complex_add(self, z1, z2):
        return z1 + z2
    
    def complex_multiply(self, z1, z2):
        return z1 * z2
    
    def complex_conjugate(self, z):
        return z.conjugate()
    
    def complex_magnitude(self, z):
        return abs(z)
    
    def complex_phase(self, z):
        return cmath.phase(z)
    
    def complex_polar(self, z):
        return cmath.polar(z)
    
    # Statistics
    def mean(self, data):
        return statistics.mean(data)
    
    def median(self, data):
        return statistics.median(data)
    
    def mode(self, data):
        try:
            return statistics.mode(data)
        except statistics.StatisticsError:
            return "No unique mode found"
    
    def std_dev(self, data, sample=True):
        if sample:
            return statistics.stdev(data)
        return statistics.pstdev(data)
    
    def variance(self, data, sample=True):
        if sample:
            return statistics.variance(data)
        return statistics.pvariance(data)
    
    def correlation(self, x, y):
        if len(x) != len(y):
            return "Error: Lists must have same length"
        return statistics.correlation(x, y)
    
    def linear_regression(self, x, y):
        if len(x) != len(y):
            return "Error: Lists must have same length"
        slope, intercept = statistics.linear_regression(x, y)
        return slope, intercept
    
    # Matrix operations
    def matrix_add(self, A, B):
        return np.add(A, B)
    
    def matrix_multiply(self, A, B):
        return np.matmul(A, B)
    
    def matrix_determinant(self, A):
        return np.linalg.det(A)
    
    def matrix_inverse(self, A):
        try:
            return np.linalg.inv(A)
        except np.linalg.LinAlgError:
            return "Error: Matrix is singular (not invertible)"
    
    def matrix_transpose(self, A):
        return np.transpose(A)
    
    def matrix_eigenvalues(self, A):
        return np.linalg.eigvals(A)
    
    # Number theory
    def is_prime(self, n):
        n = int(n)
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    def prime_factors(self, n):
        n = int(n)
        factors = []
        d = 2
        while d * d <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
            d += 1
        if n > 1:
            factors.append(n)
        return factors
    
    def nth_prime(self, n):
        if n < 1:
            return "Error: n must be positive"
        count = 0
        num = 2
        while count < n:
            if self.is_prime(num):
                count += 1
                if count == n:
                    return num
            num += 1
    
    def fibonacci(self, n):
        if n < 0:
            return "Error: n must be non-negative"
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b
    
    # Number conversions
    def bin_to_dec(self, binary):
        return int(binary, 2)
    
    def dec_to_bin(self, decimal):
        return bin(int(decimal))[2:]
    
    def hex_to_dec(self, hexadecimal):
        return int(hexadecimal, 16)
    
    def dec_to_hex(self, decimal):
        return hex(int(decimal))[2:].upper()
    
    def oct_to_dec(self, octal):
        return int(octal, 8)
    
    def dec_to_oct(self, decimal):
        return oct(int(decimal))[2:]
    
    # Bitwise operations
    def bitwise_and(self, a, b):
        return int(a) & int(b)
    
    def bitwise_or(self, a, b):
        return int(a) | int(b)
    
    def bitwise_xor(self, a, b):
        return int(a) ^ int(b)
    
    def bitwise_not(self, a):
        return ~int(a)
    
    def bit_shift_left(self, a, n):
        return int(a) << int(n)
    
    def bit_shift_right(self, a, n):
        return int(a) >> int(n)
    
    # Expression evaluation
    def evaluate_expression(self, expression):
        try:
            # Replace constants
            for const, value in self.constants.items():
                expression = expression.replace(const, str(value))
            
            # Replace variables
            for var, value in self.variables.items():
                expression = expression.replace(var, str(value))
            
            # Replace symbols
            expression = expression.replace('^', '**')
            expression = expression.replace('√', 'math.sqrt')
            
            # Safe evaluation
            allowed_names = {
                'abs': abs, 'round': round, 'min': min, 'max': max,
                'sum': sum, 'pow': pow, 'math': math, 'cmath': cmath
            }
            
            # Add math functions
            for name in dir(math):
                if not name.startswith('_'):
                    allowed_names[name] = getattr(math, name)
            
            result = eval(expression, {"__builtins__": {}}, allowed_names)
            return result
        except Exception as e:
            return f"Error: {str(e)}"
    
    # Memory operations
    def memory_store(self, value):
        self.memory = value
        return f"Stored {value} in memory"
    
    def memory_recall(self):
        return self.memory
    
    def memory_add(self, value):
        self.memory += value
        return f"Added {value} to memory (Total: {self.memory})"
    
    def memory_subtract(self, value):
        self.memory -= value
        return f"Subtracted {value} from memory (Total: {self.memory})"
    
    def memory_clear(self):
        self.memory = 0
        return "Memory cleared"
    
    # Unit conversions
    def convert_temperature(self, value, from_unit, to_unit):
        # Convert to Celsius
        if from_unit.lower() == 'f':
            celsius = (value - 32) * 5/9
        elif from_unit.lower() == 'k':
            celsius = value - 273.15
        else:
            celsius = value
        
        # Convert to target
        if to_unit.lower() == 'f':
            return celsius * 9/5 + 32
        elif to_unit.lower() == 'k':
            return celsius + 273.15
        return celsius
    
    def convert_angle(self, value, from_unit, to_unit):
        # Convert to radians
        if from_unit.lower() == 'deg':
            radians = math.radians(value)
        elif from_unit.lower() == 'grad':
            radians = value * math.pi / 200
        else:
            radians = value
        
        # Convert to target
        if to_unit.lower() == 'deg':
            return math.degrees(radians)
        elif to_unit.lower() == 'grad':
            return radians * 200 / math.pi
        return radians


class CalculatorUI:
    def __init__(self):
        self.calc = AdvancedCalculator()
        self.mode = CalculatorMode.BASIC
        
    def display_header(self):
        print("\n" + "="*60)
        print("ADVANCED SCIENTIFIC CALCULATOR".center(60))
        print(f"Mode: {self.mode.value}".center(60))
        print("="*60)
    
    def display_menu(self):
        print("\nMain Menu:")
        print("1. Basic Mode")
        print("2. Scientific Mode")
        print("3. Programmer Mode")
        print("4. Statistics Mode")
        print("5. Matrix Mode")
        print("6. Expression Evaluator")
        print("7. Unit Converter")
        print("8. Memory Functions")
        print("9. View History")
        print("10. Help")
        print("0. Exit")
    
    def basic_mode(self):
        print("\nBasic Calculator")
        print("Operations: +, -, *, /, %, //, ^")
        
        try:
            num1 = float(input("Enter first number: "))
            op = input("Enter operation (+, -, *, /, %, //, ^): ")
            num2 = float(input("Enter second number: "))
            
            operations = {
                '+': self.calc.add,
                '-': self.calc.subtract,
                '*': self.calc.multiply,
                '/': self.calc.divide,
                '%': self.calc.modulo,
                '//': self.calc.integer_divide,
                '^': self.calc.power
            }
            
            if op in operations:
                result = operations[op](num1, num2)
                print(f"\nResult: {num1} {op} {num2} = {result}")
                self.calc.last_result = result
            else:
                print("Invalid operation!")
                
        except ValueError:
            print("Invalid input!")
    
    def scientific_mode(self):
        print("\nScientific Calculator")
        print("\nCategories:")
        print("1. Trigonometric")
        print("2. Logarithmic/Exponential")
        print("3. Power/Root")
        print("4. Special Functions")
        print("5. Complex Numbers")
        print("6. Number Theory")
        
        choice = input("\nSelect category (1-6): ")
        
        if choice == '1':
            self.trigonometric_menu()
        elif choice == '2':
            self.logarithmic_menu()
        elif choice == '3':
            self.power_root_menu()
        elif choice == '4':
            self.special_functions_menu()
        elif choice == '5':
            self.complex_menu()
        elif choice == '6':
            self.number_theory_menu()
    
    def trigonometric_menu(self):
        print("\nTrigonometric Functions")
        print(f"Current angle mode: {self.calc.angle_mode}")
        print("1. sin  2. cos  3. tan")
        print("4. asin 5. acos 6. atan")
        print("7. sinh 8. cosh 9. tanh")
        print("10. Change angle mode")
        
        choice = input("\nSelect function: ")
        
        if choice == '10':
            mode = input("Enter angle mode (deg/rad/grad): ").lower()
            if mode in ['deg', 'rad', 'grad']:
                self.calc.angle_mode = mode
                print(f"Angle mode set to {mode}")
            return
        
        try:
            x = float(input("Enter value: "))
            
            functions = {
                '1': self.calc.sin, '2': self.calc.cos, '3': self.calc.tan,
                '4': self.calc.asin, '5': self.calc.acos, '6': self.calc.atan,
                '7': self.calc.sinh, '8': self.calc.cosh, '9': self.calc.tanh
            }
            
            if choice in functions:
                result = functions[choice](x)
                func_names = ['sin', 'cos', 'tan', 'asin', 'acos', 'atan', 
                             'sinh', 'cosh', 'tanh']
                print(f"\n{func_names[int(choice)-1]}({x}) = {result}")
                
        except ValueError:
            print("Invalid input!")
    
    def logarithmic_menu(self):
        print("\nLogarithmic/Exponential Functions")
        print("1. e^x")
        print("2. ln(x)")
        print("3. log10(x)")
        print("4. log2(x)")
        print("5. log_a(x) - custom base")
        
        choice = input("\nSelect function: ")
        
        try:
            if choice == '5':
                x = float(input("Enter x: "))
                base = float(input("Enter base: "))
                result = self.calc.log_base(x, base)
                print(f"\nlog_{base}({x}) = {result}")
            else:
                x = float(input("Enter value: "))
                
                functions = {
                    '1': self.calc.exp,
                    '2': self.calc.ln,
                    '3': self.calc.log10,
                    '4': self.calc.log2
                }
                
                if choice in functions:
                    result = functions[choice](x)
                    func_names = ['e^', 'ln', 'log10', 'log2']
                    print(f"\n{func_names[int(choice)-1]}({x}) = {result}")
                    
        except ValueError:
            print("Invalid input!")
    
    def power_root_menu(self):
        print("\nPower & Root Functions")
        print("1. x^y")
        print("2. sqrt(x)")
        print("3. cbrt(x)")
        print("4. nth_root(x)")
        
        choice = input("\nSelect function: ")
        
        try:
            if choice == '1':
                base = float(input("Enter base: "))
                exp = float(input("Enter exponent: "))
                result = self.calc.power(base, exp)
                print(f"\n{base}^{exp} = {result}")
            elif choice == '2':
                x = float(input("Enter value: "))
                result = self.calc.sqrt(x)
                print(f"\nsqrt({x}) = {result}")
            elif choice == '3':
                x = float(input("Enter value: "))
                result = self.calc.cube_root(x)
                print(f"\ncbrt({x}) = {result}")
            elif choice == '4':
                x = float(input("Enter value: "))
                n = float(input("Enter root degree: "))
                result = self.calc.nth_root(x, n)
                print(f"\n{n}th_root({x}) = {result}")
                
        except ValueError:
            print("Invalid input!")
    
    def special_functions_menu(self):
        print("\nSpecial Functions")
        print("1. n! (factorial)")
        print("2. nCr (combinations)")
        print("3. nPr (permutations)")
        print("4. GCD")
        print("5. LCM")
        print("6. Gamma function")
        print("7. Beta function")
        print("8. Error function")
        
        choice = input("\nSelect function: ")
        
        try:
            if choice in ['1']:
                n = int(input("Enter n: "))
                result = self.calc.factorial(n)
                print(f"\n{n}! = {result}")
            elif choice in ['2', '3']:
                n = int(input("Enter n: "))
                r = int(input("Enter r: "))
                if choice == '2':
                    result = self.calc.combination(n, r)
                    print(f"\nC({n},{r}) = {result}")
                else:
                    result = self.calc.permutation(n, r)
                    print(f"\nP({n},{r}) = {result}")
            elif choice in ['4', '5']:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                if choice == '4':
                    result = self.calc.gcd(a, b)
                    print(f"\nGCD({a},{b}) = {result}")
                else:
                    result = self.calc.lcm(a, b)
                    print(f"\nLCM({a},{b}) = {result}")
            elif choice == '6':
                x = float(input("Enter x: "))
                result = self.calc.gamma(x)
                print(f"\nGamma({x}) = {result}")
            elif choice == '7':
                x = float(input("Enter x: "))
                y = float(input("Enter y: "))
                result = self.calc.beta(x, y)
                print(f"\nBeta({x},{y}) = {result}")
            elif choice == '8':
                x = float(input("Enter x: "))
                result = self.calc.erf(x)
                print(f"\nerf({x}) = {result}")
                
        except ValueError:
            print("Invalid input!")
    
    def complex_menu(self):
        print("\nComplex Number Operations")
        print("Enter complex numbers as 'a+bj' (e.g., 3+4j)")
        
        try:
            z1 = complex(input("Enter first complex number: "))
            
            print("\n1. Addition")
            print("2. Multiplication")
            print("3. Conjugate")
            print("4. Magnitude")
            print("5. Phase")
            print("6. Polar form")
            
            choice = input("\nSelect operation: ")
            
            if choice in ['1', '2']:
                z2 = complex(input("Enter second complex number: "))
                if choice == '1':
                    result = self.calc.complex_add(z1, z2)
                    print(f"\n{z1} + {z2} = {result}")
                else:
                    result = self.calc.complex_multiply(z1, z2)
                    print(f"\n{z1} * {z2} = {result}")
            elif choice == '3':
                result = self.calc.complex_conjugate(z1)
                print(f"\nConjugate of {z1} = {result}")
            elif choice == '4':
                result = self.calc.complex_magnitude(z1)
                print(f"\n|{z1}| = {result}")
            elif choice == '5':
                result = self.calc.complex_phase(z1)
                print(f"\nPhase of {z1} = {result} radians")
            elif choice == '6':
                r, theta = self.calc.complex_polar(z1)
                print(f"\nPolar form: r={r:.4f}, theta={theta:.4f} radians")
                
        except ValueError:
            print("Invalid complex number format!")
    
    def number_theory_menu(self):
        print("\nNumber Theory Functions")
        print("1. Check if prime")
        print("2. Prime factorization")
        print("3. nth prime number")
        print("4. nth Fibonacci number")
        
        choice = input("\nSelect function: ")
        
        try:
            if choice == '1':
                n = int(input("Enter number: "))
                result = self.calc.is_prime(n)
                print(f"\n{n} is {'prime' if result else 'not prime'}")
            elif choice == '2':
                n = int(input("Enter number: "))
                result = self.calc.prime_factors(n)
                print(f"\nPrime factors of {n}: {result}")
            elif choice == '3':
                n = int(input("Enter n: "))
                result = self.calc.nth_prime(n)
                print(f"\nThe {n}th prime number is: {result}")
            elif choice == '4':
                n = int(input("Enter n: "))
                result = self.calc.fibonacci(n)
                print(f"\nThe {n}th Fibonacci number is: {result}")
                
        except ValueError:
            print("Invalid input!")
    
    def programmer_mode(self):
        print("\nProgrammer Mode")
        print("\n1. Number System Conversion")
        print("2. Bitwise Operations")
        
        choice = input("\nSelect category: ")
        
        if choice == '1':
            self.number_conversion_menu()
        elif choice == '2':
            self.bitwise_menu()
    
    def number_conversion_menu(self):
        print("\nNumber System Conversion")
        print("1. Binary to Decimal")
        print("2. Decimal to Binary")
        print("3. Hexadecimal to Decimal")
        print("4. Decimal to Hexadecimal")
        print("5. Octal to Decimal")
        print("6. Decimal to Octal")
        
        choice = input("\nSelect conversion: ")
        
        try:
            conversions = {
                '1': ('binary', self.calc.bin_to_dec),
                '2': ('decimal', self.calc.dec_to_bin),
                '3': ('hexadecimal', self.calc.hex_to_dec),
                '4': ('decimal', self.calc.dec_to_hex),
                '5': ('octal', self.calc.oct_to_dec),
                '6': ('decimal', self.calc.dec_to_oct)
            }
            
            if choice in conversions:
                input_type, func = conversions[choice]
                value = input(f"Enter {input_type} value: ")
                
                if input_type == 'decimal':
                    result = func(int(value))
                else:
                    result = func(value)
                    
                print(f"\nResult: {result}")
                
        except ValueError:
            print("Invalid input!")
    
    def bitwise_menu(self):
        print("\nBitwise Operations")
        print("1. AND")
        print("2. OR")
        print("3. XOR")
        print("4. NOT")
        print("5. Left Shift")
        print("6. Right Shift")
        
        choice = input("\nSelect operation: ")
        
        try:
            if choice in ['1', '2', '3']:
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                
                operations = {
                    '1': self.calc.bitwise_and,
                    '2': self.calc.bitwise_or,
                    '3': self.calc.bitwise_xor
                }
                
                result = operations[choice](a, b)
                op_symbols = {'1': '&', '2': '|', '3': '^'}
                print(f"\n{a} {op_symbols[choice]} {b} = {result}")
                print(f"Binary: {bin(a)} {op_symbols[choice]} {bin(b)} = {bin(result)}")
                
            elif choice == '4':
                a = int(input("Enter number: "))
                result = self.calc.bitwise_not(a)
                print(f"\n~{a} = {result}")
                print(f"Binary: ~{bin(a)} = {bin(result)}")
                
            elif choice in ['5', '6']:
                a = int(input("Enter number: "))
                n = int(input("Enter shift amount: "))
                
                if choice == '5':
                    result = self.calc.bit_shift_left(a, n)
                    print(f"\n{a} << {n} = {result}")
                else:
                    result = self.calc.bit_shift_right(a, n)
                    print(f"\n{a} >> {n} = {result}")
                    
        except ValueError:
            print("Invalid input!")
    
    def statistics_mode(self):
        print("\nStatistics Mode")
        print("Enter data values separated by commas")
        
        try:
            data = list(map(float, input("Enter data: ").split(',')))
            
            print("\n1. Mean")
            print("2. Median")
            print("3. Mode")
            print("4. Standard Deviation")
            print("5. Variance")
            print("6. All statistics")
            
            choice = input("\nSelect operation: ")
            
            if choice == '1':
                result = self.calc.mean(data)
                print(f"\nMean: {result}")
            elif choice == '2':
                result = self.calc.median(data)
                print(f"\nMedian: {result}")
            elif choice == '3':
                result = self.calc.mode(data)
                print(f"\nMode: {result}")
            elif choice == '4':
                sample = input("Sample (s) or Population (p)? ").lower() == 's'
                result = self.calc.std_dev(data, sample)
                print(f"\nStandard Deviation: {result}")
            elif choice == '5':
                sample = input("Sample (s) or Population (p)? ").lower() == 's'
                result = self.calc.variance(data, sample)
                print(f"\nVariance: {result}")
            elif choice == '6':
                print(f"\nStatistical Summary:")
                print(f"Count: {len(data)}")
                print(f"Sum: {sum(data)}")
                print(f"Mean: {self.calc.mean(data)}")
                print(f"Median: {self.calc.median(data)}")
                print(f"Mode: {self.calc.mode(data)}")
                print(f"Min: {min(data)}")
                print(f"Max: {max(data)}")
                print(f"Range: {max(data) - min(data)}")
                print(f"Sample Std Dev: {self.calc.std_dev(data, True)}")
                print(f"Sample Variance: {self.calc.variance(data, True)}")
                
        except ValueError:
            print("Invalid input!")
    
    def matrix_mode(self):
        print("\nMatrix Operations")
        print("Enter matrix rows separated by semicolons, values by commas")
        print("Example: 1,2,3;4,5,6;7,8,9")
        
        try:
            def input_matrix(name):
                rows = input(f"Enter matrix {name}: ").split(';')
                matrix = []
                for row in rows:
                    matrix.append(list(map(float, row.split(','))))
                return np.array(matrix)
            
            print("\n1. Addition")
            print("2. Multiplication")
            print("3. Determinant")
            print("4. Inverse")
            print("5. Transpose")
            print("6. Eigenvalues")
            
            choice = input("\nSelect operation: ")
            
            if choice in ['1', '2']:
                A = input_matrix('A')
                B = input_matrix('B')
                
                if choice == '1':
                    result = self.calc.matrix_add(A, B)
                    print(f"\nA + B =\n{result}")
                else:
                    result = self.calc.matrix_multiply(A, B)
                    print(f"\nA * B =\n{result}")
                    
            else:
                A = input_matrix('')
                
                if choice == '3':
                    result = self.calc.matrix_determinant(A)
                    print(f"\nDeterminant = {result}")
                elif choice == '4':
                    result = self.calc.matrix_inverse(A)
                    print(f"\nInverse =\n{result}")
                elif choice == '5':
                    result = self.calc.matrix_transpose(A)
                    print(f"\nTranspose =\n{result}")
                elif choice == '6':
                    result = self.calc.matrix_eigenvalues(A)
                    print(f"\nEigenvalues = {result}")
                    
        except Exception as e:
            print(f"Error: {e}")
    
    def expression_evaluator(self):
        print("\nExpression Evaluator")
        print("You can use: +, -, *, /, ^, sqrt(), sin(), cos(), etc.")
        print("Constants: pi, e, tau, phi")
        print("Type 'exit' to return to main menu")
        
        while True:
            expr = input("\n>>> ")
            if expr.lower() == 'exit':
                break
                
            result = self.calc.evaluate_expression(expr)
            print(f"Result: {result}")
            
            if isinstance(result, (int, float, complex)):
                self.calc.last_result = result
                save = input("Save result to variable? (y/n): ")
                if save.lower() == 'y':
                    var_name = input("Variable name: ")
                    self.calc.variables[var_name] = result
                    print(f"Saved as {var_name}")
    
    def unit_converter(self):
        print("\nUnit Converter")
        print("1. Temperature")
        print("2. Angle")
        
        choice = input("\nSelect conversion type: ")
        
        try:
            if choice == '1':
                value = float(input("Enter value: "))
                from_unit = input("From (C/F/K): ").upper()
                to_unit = input("To (C/F/K): ").upper()
                result = self.calc.convert_temperature(value, from_unit, to_unit)
                print(f"\n{value} {from_unit} = {result:.2f} {to_unit}")
                
            elif choice == '2':
                value = float(input("Enter value: "))
                from_unit = input("From (deg/rad/grad): ").lower()
                to_unit = input("To (deg/rad/grad): ").lower()
                result = self.calc.convert_angle(value, from_unit, to_unit)
                print(f"\n{value} {from_unit} = {result:.6f} {to_unit}")
                
        except ValueError:
            print("Invalid input!")
    
    def memory_functions(self):
        print("\nMemory Functions")
        print(f"Current memory: {self.calc.memory}")
        print("\n1. Store (MS)")
        print("2. Recall (MR)")
        print("3. Add (M+)")
        print("4. Subtract (M-)")
        print("5. Clear (MC)")
        
        choice = input("\nSelect function: ")
        
        try:
            if choice == '1':
                value = float(input("Enter value to store: "))
                print(self.calc.memory_store(value))
            elif choice == '2':
                print(f"Memory value: {self.calc.memory_recall()}")
            elif choice == '3':
                value = float(input("Enter value to add: "))
                print(self.calc.memory_add(value))
            elif choice == '4':
                value = float(input("Enter value to subtract: "))
                print(self.calc.memory_subtract(value))
            elif choice == '5':
                print(self.calc.memory_clear())
                
        except ValueError:
            print("Invalid input!")
    
    def run(self):
        print("\nWelcome to Advanced Scientific Calculator!")
        
        while True:
            self.display_header()
            self.display_menu()
            
            choice = input("\nSelect option: ")
            
            if choice == '1':
                self.mode = CalculatorMode.BASIC
                self.basic_mode()
            elif choice == '2':
                self.mode = CalculatorMode.SCIENTIFIC
                self.scientific_mode()
            elif choice == '3':
                self.mode = CalculatorMode.PROGRAMMER
                self.programmer_mode()
            elif choice == '4':
                self.mode = CalculatorMode.STATISTICS
                self.statistics_mode()
            elif choice == '5':
                self.mode = CalculatorMode.MATRIX
                self.matrix_mode()
            elif choice == '6':
                self.expression_evaluator()
            elif choice == '7':
                self.unit_converter()
            elif choice == '8':
                self.memory_functions()
            elif choice == '9':
                if self.calc.history:
                    print("\nCalculation History:")
                    for h in self.calc.history[-10:]:
                        print(f"{h.timestamp}: {h.expression} = {h.result}")
                else:
                    print("No history available")
            elif choice == '10':
                self.show_help()
            elif choice == '0':
                print("\nThank you for using Advanced Calculator!")
                print("Goodbye!")
                break
            else:
                print("Invalid option!")
            
            input("\nPress Enter to continue...")
    
    def show_help(self):
        print("\nHELP")
        print("="*60)
        print("This calculator supports:")
        print("- Basic arithmetic operations")
        print("- Scientific functions (trig, log, exponential)")
        print("- Complex number operations")
        print("- Matrix operations")
        print("- Statistical analysis")
        print("- Number system conversions")
        print("- Bitwise operations")
        print("- Expression evaluation")
        print("- Unit conversions")
        print("\nTips:")
        print("- Use 'ans' to reference the last result")
        print("- Constants available: pi, e, tau, phi")
        print("- You can save results to variables")


if __name__ == "__main__":
    # Install numpy: pip install numpy
    calculator_ui = CalculatorUI()
    calculator_ui.run()
