def tester(a, b) :
    print( 'Addition:\t' , a , '+' , b , '=' , a + b  )
    print( 'Subtraction:\t' , a , '-' , b , '=' , a - b )
    print( 'Multiplication:\t' , a , 'x' , b , '=' , a * b )
    print( 'Division:\t' , a , '/' , b , '=' , a / b )
    print( 'Floor Division:\t' , a , '//' , b , '=' , a // b )
    print( 'Modulos:\t' , a , '%' , b , '=' , a % b )
    print( 'Exponent:\t ' , a , '² = ' , a ** 2 , sep = '')

a = int(input("What do you want your first number to be: "))
b = int(input("Second number: "))
tester(a, b)