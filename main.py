def get_average(numbers):
    """Функція №1: знаходження середнього арифметичного"""
    return sum(numbers) / len(numbers)

def get_min_max(numbers):
    """Функція №2: пошук мінімуму та максимуму"""
    return min(numbers), max(numbers)

def get_even_numbers(numbers):
    """Функція №3: вивід парних чисел зі списку"""
    return [n for n in numbers if n % 2 == 0]

def main():
    
    data = [12, 5, 8, 20, 7, 15, 4]
    
    print(f"Список чисел: {data}")
    print(f"Середнє значення: {get_average(data)}")
    
    mi, ma = get_min_max(data)
    print(f"Мінімум: {mi}, Максимум: {ma}")
    
    print(f"Парні числа: {get_even_numbers(data)}")

if __name__ == "__main__":
    main()
