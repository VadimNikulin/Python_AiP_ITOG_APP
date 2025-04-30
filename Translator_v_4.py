import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator


class DigitalTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Digital Переводчик")
        self.root.geometry("1440x500")
        self.root.resizable(True, True)
        self.dark_mode = True
        self.theme_colors = {
            'dark': {
                'bg': '#2d2d2d', 'fg': '#ffffff', 'text_bg': '#3d3d3d', 'text_fg': '#ffffff', 'button_bg': '#4d4d4d',
                'button_fg': '#ffffff', 'entry_bg': '#3d3d3d', 'entry_fg': '#ffffff', 'frame_bg': '#2d2d2d',
                'name_company_color': '#5d9cec', 'combobox_bg': '#3d3d3d', 'combobox_fg': '#ffffff',
                'combobox_field_bg': '#3d3d3d', 'combobox_arrow_bg': '#4d4d4d', 'combobox_arrow_fg': '#ffffff'
            },
            'light': {
                'bg': '#f5f5f5', 'fg': '#000000', 'text_bg': '#ffffff', 'text_fg': '#000000', 'button_bg': '#e0e0e0',
                'button_fg': '#000000', 'entry_bg': '#ffffff', 'entry_fg': '#000000', 'frame_bg': '#f5f5f5',
                'name_company_color': '#2b73b7', 'combobox_bg': '#ffffff', 'combobox_fg': '#000000',
                'combobox_field_bg': '#ffffff', 'combobox_arrow_bg': '#e0e0e0', 'combobox_arrow_fg': '#000000'
            }
        }
        self.languages = {
            'ru': 'Русский', 'en': 'Английский', 'af': 'Африкаанс', 'am': 'Амхарский', 'ar': 'Арабский',
            'az': 'Азербайджанский', 'be': 'Белорусский', 'bg': 'Болгарский',
            'bn': 'Бенгальский', 'bs': 'Боснийский', 'ca': 'Каталанский', 'ceb': 'Себуанский',
            'co': 'Корсиканский', 'cs': 'Чешский', 'cy': 'Валлийский', 'da': 'Датский',
            'de': 'Немецкий', 'el': 'Греческий', 'eo': 'Эсперанто',
            'es': 'Испанский', 'et': 'Эстонский', 'eu': 'Баскский', 'fa': 'Персидский',
            'fi': 'Финский', 'fr': 'Французский', 'fy': 'Фризский', 'ga': 'Ирландский',
            'gd': 'Шотландский гэльский', 'gl': 'Галисийский', 'gu': 'Гуджарати', 'ha': 'Хауса',
            'haw': 'Гавайский', 'he': 'Иврит', 'hi': 'Хинди', 'hmn': 'Хмонг',
            'hr': 'Хорватский', 'ht': 'Гаитянский креольский', 'hu': 'Венгерский', 'hy': 'Армянский',
            'id': 'Индонезийский', 'ig': 'Игбо', 'is': 'Исландский', 'it': 'Итальянский',
            'iw': 'Иврит', 'ja': 'Японский', 'jw': 'Яванский', 'ka': 'Грузинский',
            'kk': 'Казахский', 'km': 'Кхмерский', 'kn': 'Каннада', 'ko': 'Корейский',
            'ku': 'Курдский (курманджи)', 'ky': 'Киргизский', 'la': 'Латинский', 'lb': 'Люксембургский',
            'lo': 'Лаосский', 'lt': 'Литовский', 'lv': 'Латышский', 'mg': 'Малагасийский', 'mi': 'Маори',
            'mk': 'Македонский', 'ml': 'Малаялам', 'mn': 'Монгольский', 'mr': 'Маратхи', 'ms': 'Малайский',
            'mt': 'Мальтийский', 'my': 'Бирманский', 'ne': 'Непальский', 'nl': 'Голландский',
            'no': 'Норвежский', 'ny': 'Чичева', 'or': 'Ория', 'pa': 'Пенджабский',
            'pl': 'Польский', 'ps': 'Пушту', 'pt': 'Португальский', 'ro': 'Румынский',
            'sd': 'Синдхи', 'si': 'Сингальский', 'sk': 'Словацкий', 'sl': 'Словенский',
            'sm': 'Самоанский', 'sn': 'Шона', 'so': 'Сомалийский', 'sq': 'Албанский', 'sr': 'Сербский',
            'st': 'Сесото', 'su': 'Суданский', 'sv': 'Шведский', 'sw': 'Суахили', 'ta': 'Тамильский',
            'te': 'Телугу', 'tg': 'Таджикский', 'th': 'Тайский', 'tl': 'Филиппинский', 'tr': 'Турецкий',
            'ug': 'Уйгурский', 'uk': 'Украинский', 'ur': 'Урду', 'uz': 'Узбекский', 'vi': 'Вьетнамский',
            'xh': 'Коса', 'yi': 'Идиш', 'yo': 'Йоруба', 'zh-CN': 'Китайский (упрощенный)',
            'zh-TW': 'Китайский (традиционный)', 'zu': 'Зулусский'
        }
        self.reversed_languages = {v.lower(): k for k, v in self.languages.items()}
        self.languages_list = sorted(list(self.languages.values()))
        self.create_widgets()
        self.apply_theme()

    def create_widgets(self):
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 16))
        style.configure('TLabel', font=('Arial', 16))
        self.top_frame = ttk.Frame(self.root)
        self.top_frame.pack(pady=10, padx=150, fill=tk.X)
        self.theme_btn = ttk.Button(self.top_frame, text="☀️", width=3, command=self.toggle_theme)
        self.theme_btn.pack(side=tk.RIGHT, padx=5)
        self.source_lang = tk.StringVar(value="Русский")
        self.source_label = ttk.Label(self.top_frame, text="Перевести с:")
        self.source_label.pack(side=tk.LEFT, padx=5)
        self.source_menu = ttk.Combobox(self.top_frame, textvariable=self.source_lang, values=self.languages_list, state="readonly")
        self.source_menu.pack(side=tk.LEFT, padx=34)
        self.swap_btn = ttk.Button(self.top_frame, text="⇄", width=3, command=self.swap_languages)
        self.swap_btn.pack(side=tk.LEFT, padx=190)
        self.target_lang = tk.StringVar(value="Английский")
        self.target_label = ttk.Label(self.top_frame, text="На:")
        self.target_label.pack(side=tk.LEFT, padx=55)
        self.target_menu = ttk.Combobox(self.top_frame, textvariable=self.target_lang, values=self.languages_list, state="readonly")
        self.target_menu.pack(side=tk.LEFT, padx=5)
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        self.source_text = tk.Text(self.main_frame, wrap=tk.WORD, font=('Arial', 12), height=10, padx=10, pady=10)
        self.source_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.translate_btn = ttk.Button(self.main_frame, text="Перевести →", command=self.translate)
        self.translate_btn.pack(side=tk.LEFT, padx=5, fill=tk.Y)
        self.target_text = tk.Text(self.main_frame, wrap=tk.WORD, font=('Arial', 12), height=10, padx=10, pady=10, state=tk.DISABLED)
        self.target_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.bottom_frame = ttk.Frame(self.root)
        self.bottom_frame.pack(fill=tk.X, padx=10, pady=10)
        self.name_company = tk.Label(self.bottom_frame, text="Digital Titan co.", font=("Julius Sans One", 32))
        self.name_company.pack(pady=20)
        self.clear_btn = ttk.Button(self.bottom_frame, text="Очистить", command=self.clear_text)
        self.clear_btn.pack(side=tk.RIGHT, padx=5)
        self.copy_btn = ttk.Button(self.bottom_frame, text="Копировать", command=self.copy_text)
        self.copy_btn.pack(side=tk.RIGHT, padx=5)

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.apply_theme()
        self.theme_btn.config(text="🌙" if self.dark_mode else "☀️")

    def apply_theme(self):
        theme = 'dark' if self.dark_mode else 'light'
        colors = self.theme_colors[theme]
        self.root.configure(bg=colors['bg'])
        style = ttk.Style()
        style.theme_use('default')
        style.configure('.', background=colors['frame_bg'], foreground=colors['fg'], fieldbackground=colors['entry_bg'], selectbackground=colors['name_company_color'], selectforeground=colors['text_fg'])
        style.configure('TFrame', background=colors['frame_bg'])
        style.configure('TLabel', background=colors['frame_bg'], foreground=colors['fg'])
        style.configure('TButton', background=colors['button_bg'], foreground=colors['button_fg'], bordercolor=colors['button_bg'], lightcolor=colors['button_bg'], darkcolor=colors['button_bg'])
        style.configure('TCombobox', fieldbackground=colors['combobox_field_bg'], foreground=colors['combobox_fg'], background=colors['combobox_bg'], arrowcolor=colors['combobox_arrow_fg'], selectbackground=colors['name_company_color'])
        style.map('TCombobox', fieldbackground=[('readonly', colors['combobox_field_bg'])], background=[('readonly', colors['combobox_bg'])], arrowcolor=[('readonly', colors['combobox_arrow_fg'])])
        self.source_text.config(bg=colors['text_bg'], fg=colors['text_fg'], insertbackground=colors['fg'])
        self.target_text.config(bg=colors['text_bg'], fg=colors['text_fg'], insertbackground=colors['fg'])
        self.name_company.config(bg=colors['frame_bg'], fg=colors['name_company_color'])
        self.top_frame.configure(style='TFrame')
        self.main_frame.configure(style='TFrame')
        self.bottom_frame.configure(style='TFrame')
        self.theme_btn.configure(style='TButton')
        self.swap_btn.configure(style='TButton')
        self.translate_btn.configure(style='TButton')
        self.clear_btn.configure(style='TButton')
        self.copy_btn.configure(style='TButton')
        self.source_label.configure(style='TLabel')
        self.target_label.configure(style='TLabel')
        self.source_menu.configure(style='TCombobox')
        self.target_menu.configure(style='TCombobox')

    def translate(self):
        input_language = self.source_lang.get()
        output_language = self.target_lang.get()
        word = self.source_text.get("1.0", tk.END).strip()
        if not word:
            messagebox.showwarning("Предупреждение", "Введите текст для перевода")
            return
        try:
            translation_result = self.translated(word, input_language, output_language)
            self.target_text.config(state=tk.NORMAL)
            self.target_text.delete("1.0", tk.END)
            self.target_text.insert(tk.END, translation_result)
            self.target_text.config(state=tk.DISABLED)
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось выполнить перевод: {str(e)}")

    def translated(self, word, input_language, output_language):
        code_inp = self.reversed_languages.get(input_language.lower(), "")
        code_out = self.reversed_languages.get(output_language.lower(), "")
        if not code_inp or not code_out:
            return "Язык не найден"
        translator = GoogleTranslator(source=code_inp, target=code_out)
        return translator.translate(word)

    def swap_languages(self):
        current_source = self.source_lang.get()
        current_target = self.target_lang.get()
        self.source_lang.set(current_target)
        self.target_lang.set(current_source)
        source_text = self.source_text.get("1.0", tk.END).strip()
        target_text = self.target_text.get("1.0", tk.END).strip() if not self.target_text.compare("end-1c", "==","1.0") else ""
        if source_text and target_text:
            self.source_text.delete("1.0", tk.END)
            self.source_text.insert("1.0", target_text)
            self.target_text.config(state=tk.NORMAL)
            self.target_text.delete("1.0", tk.END)
            self.target_text.insert("1.0", source_text)
            self.target_text.config(state=tk.DISABLED)

    def clear_text(self):
        self.source_text.delete("1.0", tk.END)
        self.target_text.config(state=tk.NORMAL)
        self.target_text.delete("1.0", tk.END)
        self.target_text.config(state=tk.DISABLED)

    def copy_text(self):
        if not self.target_text.compare("end-1c", "==", "1.0"):
            text_to_copy = self.target_text.get("1.0", tk.END).strip()
            self.root.clipboard_clear()
            self.root.clipboard_append(text_to_copy)
            messagebox.showinfo("Успех", "Текст скопирован в буфер обмена")


if __name__ == "__main__":
    root = tk.Tk()
    app = DigitalTranslator(root)
    root.mainloop()
