import sys
import builtins
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog
from app import crud_oficinas, crud_clientes


class TextRedirector:
    """Clase que redirige stdout al widget de texto de Tkinter."""

    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, s):
        """Escribe texto en el widget de texto y desplaza el scroll automáticamente."""
        self.text_widget.configure(state='normal')
        self.text_widget.insert(tk.END, s)
        self.text_widget.see(tk.END)
        self.text_widget.configure(state='disabled')

    def flush(self):
        """Método requerido por sys.stdout, pero no es necesario implementarlo aquí."""
        pass


class JardinexApp(tk.Tk):
    """Clase principal de la aplicación gráfica del sistema Jardinex."""

    def __init__(self):
        super().__init__()

        self.title("Sistema Jardinex")
        self.geometry("600x400")

        # ======================
        # Sección de botones
        # ======================
        btn_frame = tk.Frame(self)
        btn_frame.pack(side=tk.TOP, fill=tk.X, pady=10)

        # Botones de funcionalidades
        tk.Button(btn_frame, text="Listar oficinas",
                  command=lambda: self.execute(crud_oficinas.listar_oficinas)).pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text="Crear oficina",
                  command=lambda: self.execute(crud_oficinas.crear_oficina)).pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text="Listar clientes",
                  command=lambda: self.execute(crud_clientes.listar_clientes)).pack(side=tk.LEFT, padx=5)

        tk.Button(btn_frame, text="Buscar clientes por ciudad",
                  command=lambda: self.execute(crud_clientes.buscar_clientes_por_ciudad)).pack(side=tk.LEFT, padx=5)

        # ============================
        # Área de texto para la salida
        # ============================
        self.output = scrolledtext.ScrolledText(self, state='disabled', wrap=tk.WORD)
        self.output.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Redireccionar stdout al área de texto
        sys.stdout = TextRedirector(self.output)

    def clear_output(self):
        """Limpia el área de texto."""
        self.output.configure(state='normal')
        self.output.delete('1.0', tk.END)
        self.output.configure(state='disabled')

    def tk_input(self, prompt=''):
        """Función que reemplaza input() con un cuadro de diálogo."""
        return simpledialog.askstring("Entrada", prompt, parent=self)

    def execute(self, func):
        """
        Ejecuta una función, redirigiendo stdout e input
        y mostrando errores en un cuadro de diálogo si ocurren.
        """
        self.clear_output()

        # Guardar input original y redirigir a cuadro de diálogo
        original_input = builtins.input
        builtins.input = self.tk_input

        try:
            func()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
        finally:
            # Restaurar función input original
            builtins.input = original_input


if __name__ == "__main__":
    # Iniciar la aplicación
    app = JardinexApp()
    app.mainloop()
