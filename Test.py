def main (n):
    for i in range (1, n+1):
        if i % 5 == 0 and i % 3 == 0:
            print("Fizzbuzz")
        elif i % 3 == 0 :
            print("Fizz")
        elif i % 5 == 0 :
            print("Buzz")
        else : 
            print(i)
    
    


if __name__ == "__main__":
    n = int(input())
    main(n)