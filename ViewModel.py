from tkinter import *
import DataModel

cell_size = 5
is_running = False

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
    start_button.bind('<Button-1>', start_handler)
    clear_button = Button(root, text='Clear', width=12)
    clear_button.bind('<Button-1>', clear_handler)

    choice = StringVar(root)
    choice.set('Choose a Pattern')
    option = OptionMenu(root, choice, 'Choose a Pattern', 'glider', 'glider gun', 'random')
    option.config(width=20)

    grid_view.grid(row=0, columnspan=3, padx=20, pady=20)
    start_button.grid(row=1, column=0, sticky=W, padx=20, pady=20)
    option.grid(row=1, column=1, padx=20)
    clear_button.grid(row=1, column=2, sticky=E, padx=20, pady=20)


def start_handler(event):
    global is_running, start_button

    if is_running:
        is_running = False
        start_button.configure(text='Start')
    else:
        is_running = True
        start_button.configure(text='Pause')
        update()


def clear_handler(event):
    global is_running, start_button

    is_running = False

    for i in range(0, DataModel.height):
        for j in range(0, DataModel.width):
            draw_cell(i, j, 'white')


def update():
    global grid_view, root, is_running

    grid_view.delete(ALL)
    DataModel.next_gen()

    for i in range(0, DataModel.height):
        for j in range(0, DataModel.width):
            if DataModel.grid_model[i][j] == 1:
                draw_cell(i, j, 'black')
    
    if(is_running):
        root.after(100, update)


def draw_cell(row, col, color):
    global grid_view, cell_size

    if color == 'black':
        outline = 'grey'
    else:
        outline = 'white'

    grid_view.create_rectangle(row*cell_size,
                               col*cell_size,
                               row*cell_size+cell_size,
                               col*cell_size+cell_size,
                               fill=color, outline=outline)


if __name__ == '__main__':
    setup()
    update() 
    mainloop()