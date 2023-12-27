OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./build6/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window6 = Toplevel(window)
window6.geometry("900x600")
window6.configure(bg = "#1F43A0")



connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='bank',
    autocommit=True
)

cursor = connection.cursor()
def update_details(acc_value,newuser,newaddr,newage,newno,newmail):
    try:
        accno =acc_value
        new_name = newuser
        new_address =newaddr
        new_age = newage
        new_phone = newno
        new_mail=newmail

        #Check if there is no input for any field, and retrieve the existing values
        if not new_age:
            new_age = get_existing_value(accno, 'age')
        if not new_mail:
            new_mail = get_existing_value(accno, 'mail')

        if not new_phone:
            new_phone = get_existing_value(accno, 'phone')
        if not new_address:
            new_address = get_existing_value(accno, 'address')
        if not new_name:
            new_name = get_existing_value(accno, 'name')

        cursor = connection.cursor()
        update_query = "UPDATE customer SET age = %s, phone = %s, address = %s, name = %s, mail= %s WHERE account = %s"
        cursor.execute(update_query, (new_age, new_phone, new_address, new_name, new_mail,accno))
        

        connection.commit()
        cursor.close()
        connection.close()


        print("Update successful")

        # Display a pop-up box indicating the success of the update
        messagebox.showinfo("Success", "Update successful!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        feedback_label.config(text="Update failed. Check logs for details.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        feedback_label.config(text="Update failed. Check logs for details.")


def get_existing_value(acc_no, field):
    # Function to retrieve the existing value for a given field
    cursor = connection.cursor()
    select_query = f"SELECT {field} FROM customer WHERE account = %s"
    cursor.execute(select_query, (acc_no,))
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None


canvas = Canvas(
    window6,
    bg = "#1F43A0",
    height = 600,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
feedback_label = Label(
    window6, 
    text="",
    fg="red"  # You can change the color as needed
)
feedback_label.place(x=10, y=10)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    390.0,
    45.0,
    image=image_image_1
)

canvas.create_text(
    86.0,
    17.0,
    anchor="nw",
    text="Update",
    fill="#000000",
    font=("Inter Bold", 40 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    450.0,
    346.0,
    image=image_image_2
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    530.0,
    378.5,
    image=entry_image_3
)
entry_3 = Entry(
    window6,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=333.0,
    y=360.0,
    width=394.0,
    height=35.0
)
entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    530.0,
    472.5,
    image=entry_image_1
)
entry_1 = Entry(
    window6,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=333.0,
    y=454.0,
    width=394.0,
    height=35.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    530.0,
    285,
    image=entry_image_4
)
entry_4 = Entry(
    window6,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=333.0,
    y=266.0,
    width=394.0,
    height=35.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    530.0,
    331.5,
    image=entry_image_6
)
entry_6 = Entry(
    window6,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=333.0,
    y=313.0,
    width=394.0,
    height=35.0
)

entry_5 = Entry(
    window6,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=333.0,
    y=160.0,
    width=394.0,
    height=35.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    530.0,
    425.5,
    image=entry_image_2
)
entry_2 = Entry(
    window6,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=333.0,
    y=407.0,
    width=394.0,
    height=35.0
)


canvas.create_text(
    210.0,
    454.0,
    anchor="nw",
    text="Address:",
    fill="#000000",
    font=("Inter Bold", 26 * -1)
)

canvas.create_text(
    267.0,
    360.0,
    anchor="nw",
    text="Age:",
    fill="#000000",
    font=("Inter Bold", 26 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    51.0,
    46.0,
    image=image_image_3
)


submit_button = Button(
    window6,
    text="UPDATE",  # Use an appropriate image or configure as needed
    borderwidth=0,
    highlightthickness=0,
    command=lambda:update_details(entry_5.get(),entry_4.get(),entry_1.get(),entry_3.get(),entry_2.get(),entry_6.get()),
    bg="#8ca6fe",
    font="bold",
    relief="raised"
)
submit_button.place(
    x=741.0,
    y=500.0,  # Adjust the y-coordinate as needed
    width=100.0,  # Adjust the width as needed
    height=40.0
)


button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    window6,
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=380.0,
    y=500.0,
    width=155.0,
    height=43.0
)



canvas.create_text(
    267.0,
    220.0,
    anchor="nw",
    text="Enter in the fields to update",
    fill="#000000",
    font=("Inter Bold", 26 * -1)
)

canvas.create_text(
    104.0,
    160.0,
    anchor="nw",
    text="Account number:",
    fill="#000000",
    font=("Inter Bold", 26 * -1)
)

canvas.create_text(
    243.0,
    266.0,
    anchor="nw",
    text="Name:",
    fill="#000000",
    font=("Inter Bold", 26 * -1)
)

canvas.create_text(
    267.0,
    313.0,
    anchor="nw",
    text="Mail:",
    fill="#000000",
    font=("Inter Bold", 26 * -1)
)

canvas.create_text(
    127.0,
    407.0,
    anchor="nw",
    text="Phone Number:",
    fill="#000000",
    font=("Inter Bold", 26 * -1)
)

window6.resizable(False, False)
window6.mainloop()
