import tkinter as tk
import random
from tkinter import messagebox

class JogoAdivinhacao:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo da Adivinhação")
        self.root.geometry("400x300")
        self.root.resizable(False, False)

        self.frame_inicio()

    def frame_inicio(self):
       
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="🎮 Jogo da Adivinhação 🎮", font=("Arial", 16, "bold")).pack(pady=20)
        tk.Label(self.root, text="Escolha o intervalo de números:", font=("Arial", 12)).pack()

        self.entry_min = tk.Entry(self.root, justify="center")
        self.entry_min.pack(pady=5)
        self.entry_min.insert(0, "1")

        self.entry_max = tk.Entry(self.root, justify="center")
        self.entry_max.pack(pady=5)
        self.entry_max.insert(0, "100")

        tk.Label(self.root, text="Quantas tentativas?", font=("Arial", 12)).pack()
        self.entry_tentativas = tk.Entry(self.root, justify="center")
        self.entry_tentativas.pack(pady=5)
        self.entry_tentativas.insert(0, "5")

        tk.Button(self.root, text="Iniciar Jogo", command=self.iniciar_jogo, bg="green", fg="white", width=15).pack(pady=15)

    def iniciar_jogo(self):
        try:
            self.numero_min = int(self.entry_min.get())
            self.numero_max = int(self.entry_max.get())
            self.tentativas = int(self.entry_tentativas.get())

            if self.numero_min >= self.numero_max or self.tentativas <= 0:
                raise ValueError

            self.numero_sorteado = random.randint(self.numero_min, self.numero_max)
            self.frame_jogo()

        except ValueError:
            messagebox.showerror("Erro", "Digite valores válidos (mín < máx e tentativas > 0).")

    def frame_jogo(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Tente adivinhar o número entre {self.numero_min} e {self.numero_max}!", font=("Arial", 12), wraplength=380).pack(pady=15)
        self.entry_tentativa = tk.Entry(self.root, justify="center")
        self.entry_tentativa.pack(pady=10)

        self.label_info = tk.Label(self.root, text=f"Você tem {self.tentativas} tentativas.", font=("Arial", 11))
        self.label_info.pack(pady=5)

        tk.Button(self.root, text="Chutar", command=self.verificar_tentativa, bg="blue", fg="white", width=12).pack(pady=10)

    def verificar_tentativa(self):
        try:
            tentativa = int(self.entry_tentativa.get())
            if tentativa == self.numero_sorteado:
                messagebox.showinfo("Parabéns!", "🎉 Você acertou o número!")
                self.frame_inicio()
            else:
                self.tentativas -= 1
                if self.tentativas == 0:
                    messagebox.showerror("Fim de jogo", f"❌ Você perdeu! O número era {self.numero_sorteado}.")
                    self.frame_inicio()
                else:
                    dica = "maior" if tentativa < self.numero_sorteado else "menor"
                    self.label_info.config(text=f"Errou! Tente um número {dica}. Restam {self.tentativas} tentativas.")
        except ValueError:
            messagebox.showwarning("Aviso", "Digite um número válido.")


if __name__ == "__main__":
    root = tk.Tk()
    JogoAdivinhacao(root)
    root.mainloop()
