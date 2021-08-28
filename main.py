from tkinter import *
from tkinter.ttk import *
from datetime import datetime

second_counter = 0
counter = 18000
running = True

window = Tk()
window.title('Typing Test')
window.config(padx=0, pady=0)
window.geometry('600x500')
window.resizable(width=False, height=False)
window.iconbitmap('favicon.ico')
bg = PhotoImage(file='background.png')

canvas = Canvas(window, width=600, height=500)
canvas.pack(fill='both', expand=True)

canvas.create_image(0, 0, image=bg, anchor='nw')

def counter_label(label):
    def count():
        if running:
            global counter
            global second_counter
            if counter == 18000:
                display = "Press Start to Begin"
            else:
                # increase timer on second intervals
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display = string
            label['text'] = display
            label.after(1000, count)
            counter += 1
            second_counter += 1
    count()

def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    # 39 words
    text = Label(window, wraplength=160, text='Lorem ipsum dolor sit amet, consectetur adipiscing elit. '
                                              'Duis sollicitudin eros lorem, quis iaculis lectus maximus eget. '
                                              'Ut maximus ex a risus tincidunt egestas. Sed eleifend lorem '
                                              'id erat'' aliquet ''sollicitudin. Maecenas sed faucibus dui. '
                                              'Praesent vel tempus ''mauris.', font=('Times New Roman', 12))
    text_window = canvas.create_window(0, 150, anchor='nw', window=text)

    entry_box = Entry(window, textvariable=1, width=50, font=('Times New Roman', 12))
    entry_window = canvas.create_window(0, 50, height=30, anchor='nw', window=entry_box)
    entry_box.focus_set()


    def check_submission():
        if entry_box.get() == 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. ''Duis sollicitudin eros ' \
                              'lorem, quis iaculis lectus maximus eget. ''Ut maximus ex a risus tincidunt ' \
                              'egestas. Sed eleifend lorem ''id erat'' aliquet ''sollicitudin. Maecenas sed ' \
                              'faucibus dui. ''Praesent vel tempus ''mauris.':
            global counter
            # words per minute calculation. static number of words to compare to.
            words_per_minute = 39 / second_counter * 60
            wpm = Label(window, text='WPM:' + str(words_per_minute), font=('Times New Roman', 28))
            wpm_window = canvas.create_window(400, 0, anchor='nw', window=wpm)

    submit = Button(window, text="Submit", width=10, command=lambda: check_submission())
    submit_window = canvas.create_window(520, 500, height=80, width=80, anchor='sw', window=submit)


timer_label = Label(window, text='Press Start to Begin', font=('Times New Roman', 28))
timer_window = canvas.create_window(0, 0, anchor='nw', window=timer_label)

start = Button(window, text='Start', command=lambda: Start(timer_label))
start_window = canvas.create_window(0, 500, height=80, width=80, anchor='sw', window=start)


window.mainloop()
