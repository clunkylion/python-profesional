# hola 3 -> holaholahola
#jose 4 -> josejosejosejose

def make_repeater_of(n):
    def repeater(string):
        #si el usuario pasa un numero se lanza error
        assert type(string) == str, "string must be a string"
        return string * n
    return repeater

def main():
    repeat_5 = make_repeater_of(5)
    print(repeat_5("hola"))

if __name__ == '__main__':
    main()