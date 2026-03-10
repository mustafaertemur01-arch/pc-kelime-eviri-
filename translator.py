import keyboard
import pyautogui
from deep_translator import GoogleTranslator
import pyperclip
import time

source_lang = 'tr'
target_lang = 'en'

def translate_line():
    try:
        time.sleep(0.05)  # yazıyı yakalamak için kısa bekleme

        pyautogui.hotkey('ctrl', 'a')  # tüm yazıyı seç
        pyautogui.hotkey('ctrl', 'c')  # kopyala
        text = pyperclip.paste()

        if not text or text.strip() == "":
            print("Seçili metin boş, çevrilmedi!")
            return

        words = text.split()
        translated_words = []
        for w in words:
            try:
                tw = GoogleTranslator(source=source_lang, target=target_lang).translate(w)
                translated_words.append(tw)
            except:
                translated_words.append(w)

        translated = " ".join(translated_words)

        pyautogui.press('backspace')  # eski metni sil
        pyautogui.write(translated)   # çeviriyi yaz

    except Exception as e:
        print("Hata:", e)

keyboard.add_hotkey('F8', translate_line)  # Artık F8 ile çevir
print("Doğrudan kelime çevirisi hazır! F8 ile çevir...")
keyboard.wait()