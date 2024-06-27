from tkinter import *
import DataModel

cell_size = 5

def setup():
    global root, grid_view, cell_size, start_button, clear_button, choice

    root = Tk()
    root.title('The Game Of Life')

    grid_view = Canvas(root, width=DataModel.width*cell_size,
                     height=DataModel.height*cell_size,
                     borderwidth=0,
                     highlightthickness=0,
                     bg='white')
    
    start_button = Button(root, text='Start', width=12)
    clear_button = Button(root, text='Clear', width=12)

    choice = StringVar(root)
    choice.set('Choose a Pattern')
    option = OptionMenu(root, choice, 'Choose a Pattern', 'glider', 'glider gun', 'random')
    option.config(width=20)

    grid_view.pack()
    start_button.pack()
    option.pack()
    clear_button.pack()


if __name__ == '__main__':
    setup()
    mainloop()