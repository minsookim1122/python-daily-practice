numbers = [10, 10, 2 ,5]

def find_second_largest(numbers: list[int]) -> int:
    largest = numbers[0]
    second_largest : int | None = None
    



    
    for i in numbers:
        if i > largest:
            
            second_largest = largest
            largest = i
            

        elif i < largest and (second_largest is None or i > second_largest):
            second_largest = i

    

    return second_largest 




def main() -> None:

    print(find_second_largest(numbers))
    print(find_second_largest([3, 8, 2, 10, 5]))
    print(find_second_largest([-5, -2, -9]))
    print(find_second_largest([10, 10, 8, 5]))

    



if __name__ == "__main__":
    main()