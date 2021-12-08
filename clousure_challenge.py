def make_division_by(n):
    return lambda x: x / n

def main():
    division_by_3 = make_division_by(3)
    print((division_by_3(18)))
    
if __name__ == '__main__':
    main()