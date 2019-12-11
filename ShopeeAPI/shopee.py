import inquirer
from colr import color, Colr as C
from pyfiglet import Figlet
import os
import constants
from endpoints import Shop


class Run:
    options = ""
    themeCustom = inquirer.themes.load_theme_from_dict(constants.THEME)
    
    def __init__(self):

        self.clear()
        self.info()
        self.next()
        self.process()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def next(self):
        print("\n\n\n")

    def info(self):
        f = Figlet(font='smslant')
        print(color(f.renderText('Shopee'), fore=constants.DANGER))
        print(C().hex(constants.INFO, "Author: ").hex(constants.WARNING, "Kevin Jonathan (https://github.com/kevinjon27)"))
        print(C().hex(constants.INFO, "Github: ").hex(constants.WARNING, "https://github.com/kevinjon27"))
        print(C().hex(constants.INFO, "Email: ").hex(constants.WARNING, "kevinjonathan2701@gmail.com"))
        print(C().hex(constants.INFO, "Version: ").hex(constants.WARNING, "1.0"))

    
    def process(self):
        questions = [
            inquirer.List('opt',
                message="Select an option?",
                choices=[
                    'Get seller products',
                    'Exit'
                    ],
            ),
        ]
        answers = inquirer.prompt(questions, theme=self.themeCustom)
        self.list(answers['opt'])

    def list(self, opt):
        if opt == "Get seller products":
            Shop().productDetail()
        elif opt == "Exit":
            exit('Bye')

if __name__ == '__main__':
    Run()