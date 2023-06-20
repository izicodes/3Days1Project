from colorama import Fore, Style

rt = Fore.RED
mt = Fore.MAGENTA
gt = Fore.GREEN
ct = Fore.CYAN
bt = Fore.BLUE
yt = Fore.YELLOW

bs = Style.BRIGHT
rs = Style.RESET_ALL
ds = Style.DIM


def red(x):
	print(rt + x + rs)


def green(x):
	print(gt + x + rs)


def cyan(x):
	print(ct + x + rs)
