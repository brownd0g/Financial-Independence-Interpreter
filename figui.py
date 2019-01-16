'''

Assignment 3

Andrew Brown

'''


from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox



def getFileName(*args):
    ''' This function prompts user to open a file then calculates max, min and average.

        A file will be opened from a previous FIT test
        The function makes a list of all the final year balances from all the simulations
        It then converts the list from strings to floats
        Necessary values are assigned to variables
        If the function can not read the file properly, an error box will appear


    '''
    filename = askopenfilename()
    try:
        file =  open(filename, "r")
    
        line_string = file.readlines()
    
        final_year_list = []

        for i in range(len(line_string)):
            temp_list = line_string[i].split()
            for item in temp_list:
                if item == "Successful!" or item == "Unsuccessful":
                    temp_list.remove(item)
            final_year_list.append(temp_list[-1])

        float_list = [float(i) for i in final_year_list]

        maximum.set(max(float_list))
        minimum.set(min(float_list))

        average.set("{0: .2f}".format(sum(float_list)/float(len(float_list))))

    except:
        messagebox.showinfo(message='Error: Problem reading file\n\nPlease try again')
    


root = Tk()
root.title('FI GUI')
root.geometry("400x200")



frame = ttk.Frame(root, padding='30 5 30 30')
frame.grid(column=0, row=0, columnspan=3, sticky=(N, W, E, S))
frame.columnconfigure(0, weight=1)
frame.rowconfigure(0, weight=1)


maximum = StringVar()
minimum = StringVar()
average = StringVar()

maximum.set(0)
minimum.set(0)
average.set(0)

open_button = ttk.Button(frame, text='Open', command=getFileName)
open_button.grid(column=1, row=0, columnspan=2)

font_size = 20

max_label = ttk.Label(frame, text='Maximum Balance: $')
max_label.grid(column=1, row=2, sticky=E)
max_label.config(font=(20))

max_num = ttk.Label(frame, textvariable=maximum)
max_num.grid(column=2, row=2, sticky=(E, W))
max_num.config(font=(32))

min_label = ttk.Label(frame, text='Minimum Balance: $')
min_label.grid(column=1, row=4, sticky=E)
min_label.config(font=(32))

min_num = ttk.Label(frame, textvariable=minimum)
min_num.grid(column=2, row=4, sticky=(E, W))
min_num.config(font=(32))

average_label = ttk.Label(frame, text='Average Balance: $')
average_label.grid(column=1, row=6, sticky=E)
average_label.config(font=(32))

average_num = ttk.Label(frame, textvariable=average)
average_num.grid(column=2, row=6, sticky=(E, W))
average_num.config(font=(32))

open_button.focus()


root.bind('<Return>', getFileName)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


frame.columnconfigure(0, weight=3)
frame.columnconfigure(1, weight=3)
frame.columnconfigure(2, weight=3)
frame.columnconfigure(3, weight=3)






root.mainloop()

