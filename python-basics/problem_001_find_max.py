numbers = [3, 8, 2, 10, 5]

def find_max(numbers: list[int]) -> int:
    largest = numbers[0]

    for i in numbers:
        if i > largest:
                largest = i 

    return largest 



def main() -> None:
     print(find_max(numbers))
     print(find_max([-5, -2, -9]))
           
if __name__ == "__main__":
    main()