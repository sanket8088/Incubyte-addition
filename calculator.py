import re

class Calculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        
        if numbers.startswith("//"):
            delimiter, numbers = self._parse_delimiter(numbers)
        else:
            delimiter = ",|\n"
        
        nums = re.split(delimiter, numbers)
        int_nums = list(map(int, nums))

        negative_nums = []
        for num in int_nums:
            if num < 0:
                negative_nums.append(num)
        if negative_nums:
            raise ValueError(f"negative numbers not allowed {','.join(map(str, negative_nums))}")

        return sum(int_nums)

    def _parse_delimiter(self, numbers: str):
        delimiter_end = numbers.find('\n')
        delimiter = numbers[2:delimiter_end]
        numbers = numbers[delimiter_end + 1:]
        if delimiter.startswith('[') and delimiter.endswith(']'):
            delimiter = delimiter[1:-1]
        return f"({delimiter})", numbers
