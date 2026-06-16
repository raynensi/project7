#project7.py 
def create_file(filename):
    with open(filename, 'w') as f:
        pass
    print('File Created Successfully!')

def write_file(filename, data):
    with open(filename, 'w') as f:
        f.write(data)
        print('File Data written Successfully!')

def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content=f.read()
        print('File content:')
        print('content')
    except FilenotfoundError:    
        print('File  not found!')

def append_file(filename, data):
    with open(filename,'a') as f:
        f.write(data)
    print('Data Append Successfully!')

import datetime
import time
import match
import random
import string
import uuid
import dir
import project7

def datetime_menu():
    while True:
        print('''\nDatetime and time operations:
        \n1. Display current date and time.
        \n2. Calculate difference between two dates/times.
        \n3. Formate date into costom Formate
        \n4. Stopwatch
        \n5. Countdown Timer
        \n6. Back to Main Menu''')

        ch = input('Enter your choice: ')

        if ch=='1':
            now=datetime.datetime.now()
            print(f"Current date and time :{now.strftime('%Y-%m-%d %H:%M:%S')}")

        elif ch=='2':
            d1=input('Enter the first date (YYYY-MM-DD):')
            d2=input('Enter the second date (YYYY-MM-DD):')
            date1=datetime.datetime.strptime(d1,'%Y-%m-%d')
            date2=datetime.datetime.strptime(d2,'%Y-%m-%d')
            diff=abs((date2-date1).days)
            print(f"Difference:{diff} days")

        elif ch=='3':
            dt=datetime.datetime.now()
            fmt=input(" Enter formate: ")
            print('Formatted date:', dt.strftime(fmt))
        
        elif ch=='4':
            input('Press Enter to start stopwatch....')
            start=time.time()
            input('Press Enter to stop....')
            end=time.time()
            print(f"Elapsed time: {round(end-start,2)} seconds")

        elif ch=='5':
            sec=int(input("Enter seconds for countdown:")) 
            for i in range(sec, 0, -1):
                print(i, end="")
                time.sleep(1)
            print("\nTime's up!")

        elif ch=="6":
            break

        print("=" * 25)

def match_menu():
    while True:
        print('\nmathematical operations')
        print('1. Calculate factorial')
        print('2. Solve compound interest')
        print('3. Trigonomatric calculatiopns ')
        print('4. Area of Geomatric shapes')
        print('5. Back to main Menu ')

        ch = input('Enter your choice: ')
        if ch == '1':
            n = int(input("Enter a number: "))
            print("Factorial:", math.factorial(n))
        
        elif ch == '2':
            p = float(input("Enter principal amount: "))
            r = float(input("Enter rate of interest (in %): "))
            t = float(input("Enter time (in years): "))
            ci = p * (pow((1 + r/100), t))
            print(f"Compound Interest: {ci:.2f}")
        
        elif ch == '3':
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)
            print(f"Sin: {math.sin(rad):.2f}, Cos: {math.cos(rad):.2f}, Tan: {math.tan(rad):.2f}")
        
        elif ch == '4':
            r = float(input("Enter radius: "))
            print(f"Area of Circle: {math.pi * r * r:.2f}")
        
        elif ch == '5':
            break
        
        print("=" * 25)

def random_menu():
    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        ch = input('Enter your choice: ')

        if ch=="1":
            a= int(input('Enter lower limit:'))
            b= int(input('Enter upper limit:'))
            print(random.randint(a,b))

        elif ch=='2':
            n=int(input('Enter list size:'))
            lst=[random.randint(1,00) for _ in range(n)]
            print("Randome list:", lst)

        elif ch=='3':
            len=int(input('Enter password lebngth:'))
            cpwd=''.join([randome.choice])
            print(Generate Password:, pwd)

        elif ch=='4':
            otp=''.join([str(random.randint(0,9)) for _ in range(6)])
            print("Generate OTP:", otp)
        
        elif ch=='5':
            break

def uuid_menu():
    print(" \nGenerate Unique Identifiers:")
    print(" \nGenerate UUID:", uuid.uuid4())
    print("=" * 25)

def file_menu():
    while True:
        print('''\nFile Operatios:
        \n1. Create a new file
        \n2. Write to  a  file  
        \n3. Read from a file  
        \n4. Appnd to a file  
        \n5. Back to main menu''')

        ch = input('Enter your choice: ')
        
        if ch=='1':
            fname=input('Enter file name:')
            project7.create_file(fname)

        elif ch=='2':
            fname=input('Enter file name:')
            data=input('Enter data to write:')
            project7.write_file(fname, data)

        elif ch=='3':
            fname=input('Enter file name:')
            project7.read_file(fname)
        
        elif ch=='4':
            fname=input('Enter file name:')
            data=input('Enter data to append:')
            project7.append_file(fname, data)

        elif ch=='5':
            break

        print("="*25)

def dir_menu():
    module_name=input('\nEnter module name to explare:')
    try:
        module=__import__(module_name)
        print(f"Available attributes in {module_name} module:")
        print(dir(module))
    except:
        print("Module not found")
    print("="*25)

def main():
    while True:
        print('\n' + "="*25)
        print("Welcome to multi Utility Toolkit")
        print('Choose an option:')
        print('1. Datetime and time operation')
        print('2. Mathematical operations')
        print('3. Random data generation')
        print('4. Generate Unique Identifiers (UUID)')
        print('5. fILE OPERATION (Custom Module)')
        print('6. Explore Module Attribute(dir())')
        print('7. Exit')

        choice=input("Enter your choice: ")
        if choice=='1':
            datetime_menu()
        elif choice=='2':
            math_menu()
        elif choice=='3':
            random_menu()
        elif choice=='4':
            uuid_menu()
        elif choice=='5':
            file_menu()
        elif choice=='6':
            dir_menu()
        elif choice=='7':
            print("\n"+"="*25)
            prit('Thank you for using th multi-utility toolkit')
            break
        else:
            print('Invalid')

if __name__=="__main__":
    main()