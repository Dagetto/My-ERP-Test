from tkinter import Tk
import view


class ControladorPoo:
    def __init__(self, root):

        self.root_controler = root
        self.objeto_vista = view.ventana_interfaz(
            self.root_controller
        )

    if __name__ == "__main__":
        main = Tk()
        objeto1_controlador = view.MyErpApp(main)
        main.mainloop()
