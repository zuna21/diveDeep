from tkinter import *
from tkinter import messagebox

# function for saving links in two files, one for user if he want to read data,
# second file is for program to find a link
def save():
    link = link_entry.get()
    category = category_entry.get().lower()
    name = name_entry.get().lower()

    if link and category and name:
        with open("data/links.txt", "a") as links_file:
            links_file.write(f"{name} | {category} | {link}\n")
            link_entry.delete(0, END)
            category_entry.delete(0, END)
            name_entry.delete(0, END)

        with open("data/data.txt", "a") as data_file:
            data_file.write(f"|{name},{category},{link}")

        messagebox.showinfo(title="Saved", message="The link is saved in file data/links.txt!")

    else:
        messagebox.showerror(title="error", message="You need to enter all fields (link, category and site name)!")


# function for searching links by name or category
def find_link():
    result_entry.delete(0, END)
    search = search_entry.get().lower()
    with open("data.txt") as data_file:
        data = data_file.read()

    data = data.split("|")[1:]
    results = []
    for packet in data:
        packet = packet.split(",")
        if search in packet:
            results.append(packet[2])

    final_string = ''
    for result in results:
        final_string += result + "      |      "

    if final_string:
        result_entry.insert(0, final_string)
    else:
        messagebox.showerror(title="error", message="Sorry, you need to enter corrent name or category!")



window = Tk()
window.title('Dive Deep')
window.config(padx=20, pady=20, bg="#3d7080")

# Image in header
canvas = Canvas(height=400, width=800, bg="#3d7080", highlightthickness=0)
logo_img = PhotoImage(file='images/giphy.gif')
canvas.create_image(200, 200, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
link_label = Label(text="Link", bg="#3d7080")
link_label.grid(row=1, column=0)
category_label = Label(text="Category", bg="#3d7080")
category_label.grid(row=2, column=0)
site_name_label = Label(text="Site name", bg="#3d7080")
site_name_label.grid(row=3, column=0)

search_label = Label(text="Search by name or category", bg="#3d7080")
search_label.grid(row=5, column=0)

# Entries
link_entry = Entry(width=80, bg="#316170")
link_entry.grid(row=1, column=1)
link_entry.focus()
category_entry = Entry(width=80, bg="#316170")
category_entry.grid(row=2, column=1)
name_entry = Entry(width=80, bg="#316170")
name_entry.grid(row=3, column=1)

search_entry = Entry(width=80, bg="#316170")
search_entry.grid(row=5, column=1)

result_entry = Entry(width=80, bg="#316170")
result_entry.grid(row=7, column=1)

# Button
add_button = Button(text="ADD", width=32, bg="#2e839e", command=save)
add_button.grid(row=4, column=1)
search_button = Button(text="SEARCH", width=32, bg="#2e839e", command=find_link)
search_button.grid(row=6, column=1)

window.mainloop()