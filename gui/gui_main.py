"""Gelişmiş AIv1 GUI: tema, geçmiş, profil, ayarlar, modüller, ses, offline, dialog, gelişmiş widget'lar."""
from __future__ import annotations

import tkinter as tk
from tkinter import messagebox, filedialog, colorchooser

from config.gui_preferences import prefs
from modules.voice_assistant import speak
from .gui_elements import button, entry, label
from .themes import apply_theme, THEMES

# --- EKSTRA FONKSİYONLAR ---
def save_history(messages):
    filename = filedialog.asksaveasfilename(defaultextension=".txt")
    if filename:
        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(messages))

def change_avatar(app):
    file = filedialog.askopenfilename(title="Profil resmi seç", filetypes=[("Resimler", "*.png;*.jpg;*.jpeg")])
    if file:
        try:
            from PIL import Image, ImageTk
            img = Image.open(file)
            img = img.resize((48, 48))
            app.avatar_img = ImageTk.PhotoImage(img)
            app.avatar_label.config(image=app.avatar_img)
        except Exception:
            messagebox.showerror("Hata", "Profil resmi yüklenemedi (Pillow kurulu mu?)")

def edit_theme(app):
    col = colorchooser.askcolor(title="Arka plan rengi")
    if col and col[1]:
        app.root.configure(bg=col[1])
        for widget in app.root.winfo_children():
            try:
                widget.configure(bg=col[1])
            except Exception:
                pass

class DummyRoot:
    """Minimal stand-in for :class:`tkinter.Tk` in headless environments."""
    def __init__(self) -> None:
        self._config: dict[str, str] = {}
        self._title = "AIv1"
    def configure(self, **opts: str) -> None:
        self._config.update(opts)
    def cget(self, key: str) -> str:
        return self._config.get(key, "")
    def winfo_children(self):
        return []
    def title(self, value: str | None = None) -> str:
        if value is not None:
            self._title = value
        return self._title
    def destroy(self) -> None:
        pass
    def mainloop(self) -> None:
        pass

class AppGUI:
    """Gelişmiş, profesyonel, çok özellikli, modern görünümlü AIv1 GUI."""

    def __init__(self):
        try:
            self.root = tk.Tk()
            self._headless = False
        except tk.TclError:
            self.root = DummyRoot()
            self._headless = True

        self.root.title("AIv1 - Akıllı Yardımcı")
        apply_theme(self.root, prefs.theme)
        self.messages = []
        self.create_menu()
        self.create_left_panel()
        self.create_main_panel()
        self.create_status_bar()
        self.avatar_img = None

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        # Dosya
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Geçmişi Kaydet", command=lambda: save_history(self.messages))
        file_menu.add_separator()
        file_menu.add_command(label="Çıkış", command=self.root.quit)
        menubar.add_cascade(label="Dosya", menu=file_menu)
        # Ayarlar
        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="Tema Düzenle", command=lambda: edit_theme(self))
        settings_menu.add_command(label="Profil Resmi", command=lambda: change_avatar(self))
        settings_menu.add_separator()
        settings_menu.add_command(label="Ses Aç/Kapat", command=self.toggle_voice)
        settings_menu.add_command(label="Offline Mod", command=self.toggle_offline)
        menubar.add_cascade(label="Ayarlar", menu=settings_menu)
        # Hakkında
        about_menu = tk.Menu(menubar, tearoff=0)
        about_menu.add_command(label="Hakkında", command=lambda: messagebox.showinfo(
            "AIv1", "Yapay zeka destekli asistan arayüzü.\nTasarım: Nejux"))
        menubar.add_cascade(label="Yardım", menu=about_menu)

    def create_left_panel(self):
        frame = tk.Frame(self.root, width=140, bg="#f0f0f0")
        frame.pack(side=tk.LEFT, fill=tk.Y, padx=2, pady=2)
        self.avatar_label = tk.Label(frame, text="Profil", width=10)
        self.avatar_label.pack(pady=8)
        btn1 = tk.Button(frame, text="Modüller", command=self.show_modules)
        btn1.pack(fill=tk.X, pady=2)
        btn2 = tk.Button(frame, text="Geçmiş", command=self.show_history)
        btn2.pack(fill=tk.X, pady=2)
        btn3 = tk.Button(frame, text="Ayarlar", command=self.show_settings)
        btn3.pack(fill=tk.X, pady=2)

    def create_main_panel(self):
        frame = tk.Frame(self.root, bg="#ffffff")
        frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=2, pady=2)
        label(frame, "Mesajınızı yazın:")
        self.text_entry = entry(frame)
        send_btn = tk.Button(frame, text="Gönder", command=self._on_send)
        send_btn.pack(padx=5, pady=5)
        self.output = label(frame, "")
        # Mesaj geçmişi (chat gibi)
        self.history_box = tk.Listbox(frame, height=9, bg="#eaeaea")
        self.history_box.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

    def create_status_bar(self):
        self.status = tk.Label(self.root, text="Hazır", anchor=tk.W, bg="#dddddd")
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def show_modules(self):
        messagebox.showinfo("Modüller", "Tüm entegre edilen modüller burada listelenebilir.")

    def show_history(self):
        if not self.messages:
            messagebox.showinfo("Geçmiş", "Henüz mesaj yok.")
        else:
            hist = "\n".join(self.messages[-10:])
            messagebox.showinfo("Geçmiş (son 10)", hist)

    def show_settings(self):
        info = f"Tema: {prefs.theme}\nSes: {'Açık' if prefs.voice_enabled else 'Kapalı'}\nDil: {prefs.language}"
        messagebox.showinfo("Ayarlar", info)

    def _on_send(self):
        text = self.text_entry.get()
        if not text.strip():
            messagebox.showwarning("Uyarı", "Boş mesaj gönderilemez.")
            return
        self.messages.append(text)
        self.history_box.insert(tk.END, text)
        self.output.config(text=text)
        self.status.config(text="Son mesaj gönderildi.")
        if prefs.voice_enabled:
            speak(text)
        self.text_entry.delete(0, tk.END)

    def toggle_voice(self):
        prefs.toggle_voice()
        state = "açık" if prefs.voice_enabled else "kapalı"
        self.status.config(text=f"Ses {state}")
        messagebox.showinfo("Ses Ayarı", f"Ses artık {state}")

    def toggle_offline(self):
        prefs.voice_enabled = False
        self.status.config(text="Offline mod aktif")
        messagebox.showinfo("Offline Mod", "Uygulama offline moda geçti.")

    def run(self):
        self.root.mainloop()

def run() -> str:
    app = AppGUI()
    if not app._headless:
        app.root.update()
        title = app.root.title()
        app.root.destroy()
    else:
        title = "AIv1"
    return title
