import os


def ex_1():
    encription_cmd = "python main.py -encryption -genKeys -text \"Przykładowy tekst\""
    decription_cmd = "python main.py -decryption"
    os.system("echo === EX 1 ===")
    os.system(f"echo {encription_cmd}")
    os.system(encription_cmd)
    os.system("echo .")
    os.system(f"echo {decription_cmd}")
    os.system(decription_cmd)
    os.system("echo .")
    os.system("echo '")


def ex_2():
    encription_cmd = "python main.py -encryption -text \"Ciekawostki nr 1\""
    decription_cmd = "python main.py -decryption"
    os.system("echo === EX 2 ===")
    os.system(f"echo {encription_cmd}")
    os.system(encription_cmd)
    os.system("echo .")
    os.system(f"echo {decription_cmd}")
    os.system(decription_cmd)
    os.system("echo .")
    os.system("echo '")


def ex_3():
    encription_cmd = "python main.py -encryption -text \"Ciekawostki nr 2\" -encryptedFile ciekawostki.txt"
    decription_cmd = "python main.py -decryption -encryptedFile ciekawostki.txt"
    os.system("echo === EX 3 ===")
    os.system(f"echo {encription_cmd}")
    os.system(encription_cmd)
    os.system("echo .")
    os.system(f"echo {decription_cmd}")
    os.system(decription_cmd)
    os.system("echo .")
    os.system("echo '")


def ex_4():
    file_name = "tekst1.txt"
    encription_cmd = f"python main.py -encryption -genKeys -loadText {file_name}"
    decription_cmd = "python main.py -decryption"
    os.system("echo === EX 4 ===")
    os.system(f"echo Polska wyszła z grupy > {file_name}")
    os.system(f"echo {encription_cmd}")
    os.system(encription_cmd)
    os.system("echo .")
    os.system(f"echo {decription_cmd}")
    os.system(decription_cmd)
    os.system("echo .")
    os.system("echo '")


def ex_5():
    file_name = "tekst2.txt"
    encription_cmd = f"python main.py -encryption -loadText {file_name}"
    decription_cmd = "python main.py -decryption"
    os.system("echo === EX 5 ===")
    os.system(
        f"echo Polska vs Francja (1/8 Finału) > {file_name}")
    os.system(f"echo {encription_cmd}")
    os.system(encription_cmd)
    os.system("echo .")
    os.system(f"echo {decription_cmd}")
    os.system(decription_cmd)
    os.system("echo .")
    os.system("echo '")


def ex_6():
    encription_cmd = "python main.py -encryption -genKeys -text Piłka"
    decription_cmd = "python main.py -decryption -save odszyfrowanyTekst.txt"
    os.system("echo === EX 6 ===")
    os.system(f"echo {encription_cmd}")
    os.system(encription_cmd)
    os.system("echo .")
    os.system(f"echo {decription_cmd}")
    os.system(decription_cmd)
    os.system("echo .")
    os.system("echo '")


def ex_7():
    encription_cmd = f"python main.py -encryption -genKeys -text \"Ciekawe kto będzie w 1/4 finale?\" -showEncryptedText"
    decription_cmd = "python main.py -decryption"
    os.system("echo === EX 7 ===")
    os.system(f"echo {encription_cmd}")
    os.system(encription_cmd)
    os.system("echo .")
    os.system(f"echo {decription_cmd}")
    os.system(decription_cmd)
    os.system("echo .")
    os.system("echo '")


ex_1()
ex_2()
ex_3()
ex_4()
ex_5()
ex_6()
ex_7()
