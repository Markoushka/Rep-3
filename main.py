import colorama

#Меняет цвет, фон и яркость текста

from colorama import init
init()
from colorama import Fore, Back, Style
print(Fore.GREEN + "зеленый текст")
print(Back.YELLOW + "на желтом фоне")
print(Style.BRIGHT + "стал ярче" + Style.RESET_ALL)
print("обычный текст")

#Так же все описаное в прошлом пункте можно сделать так

print("\033[31m" + "красный текст")
print("\033[39m")


#Если в начале указать что текст должен терять все еффекты
#то при следуйщем принте они уйдут

from colorama import init, Fore
init(autoreset=True)
print(Fore.GREEN + "зеленый текст")
print("автоматический возврат к обычному")



#А вот все цвета, фоны, яркости текста
# // цвет текста
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# // цвет фона
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# // яркость текста и общий сброс
# Style: DIM, NORMAL, BRIGHT, RESET_ALL