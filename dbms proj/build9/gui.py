OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./build9/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Toplevel(window)
window.title("Loan Status")
window.geometry("800x600")
window.configure(bg = "#1F43A0")


canvas = Canvas(
    window,
    bg = "#1F43A0",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    400.0,
    45.0,
    image=image_image_1
)

canvas.create_text(
    85.0,
    25.0,
    anchor="nw",
    text="Loan",
    fill="#000000",
    font=("Inter Medium", 40 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    401.0,
    347.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    54.0,
    51.0,
    image=image_image_3
)
window.resizable(False, False)
window.mainloop()
