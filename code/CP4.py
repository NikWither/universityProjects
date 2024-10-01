def main(**kwargs):
    values = kwargs.values()

    return sum(values) / len(values)

if __name__ == "__main__":
    result = main(a=10, b=20, c=30, d=40)
    print(f"Среднее арифметическое: {result}")