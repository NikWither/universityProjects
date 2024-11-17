def read_file(filename):
    try:
        file = open(filename, 'r', encoding='utf-8')
        content = file.read()
        if not content:
            raise Exception(f"Файл {filename} пустой")
        print(f"Tекст:\n {content}")
    except Exception as ex:
        print(ex)
    finally:
        print("####################################")


if __name__ == '__main__':
    read_file('test1.txt') # пустой
    read_file('test2.txt') # не пустой