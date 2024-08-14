import tkinter as tk
from tkinter import ttk, messagebox
import phonenumbers
from phonenumbers import geocoder, carrier

# Telefon numarası bilgisi saklamak için sınıf
class PhoneNumberInfo:
    def __init__(self, number, country, operator):
        self.number = number
        self.country = country
        self.operator = operator

# Numara bilgilerini al
def get_phone_number_info():
    phone_numbers = text_area.get("1.0", tk.END).strip().splitlines()
    table_data.clear()

    for number in phone_numbers:
        if not number.startswith("+"):
            number = "+" + number.strip()

        try:
            parsed_number = phonenumbers.parse(number)
            country = geocoder.description_for_number(parsed_number, "en")
            operator = carrier.name_for_number(parsed_number, "en")
            table_data.append(PhoneNumberInfo(number, country, operator))
        except phonenumbers.NumberParseException:
            table_data.append(PhoneNumberInfo(number, "Invalid Number", "Invalid Number"))

    update_table()

# Tabloyu güncelle
def update_table():
    for row in table.get_children():
        table.delete(row)
    
    for info in table_data:
        table.insert('', 'end', values=(info.number, info.country, info.operator))

# Ana pencere
root = tk.Tk()
root.title("Phone Number Information")
root.geometry("600x400")

# Giriş alanı
label = tk.Label(root, text="Enter Phone Numbers (One per line):")
label.pack(pady=10)

text_area = tk.Text(root, height=10)
text_area.pack(fill=tk.X, padx=10)

# Bilgileri al butonu
button = tk.Button(root, text="Get Information", command=get_phone_number_info)
button.pack(pady=10)

# Sonuç tablosu
columns = ("Number", "Country", "Operator")
table = ttk.Treeview(root, columns=columns, show='headings')
table.heading("Number", text="Number")
table.heading("Country", text="Country")
table.heading("Operator", text="Operator")
table.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Tablo verilerini saklamak için liste
table_data = []

# Uygulama döngüsü
root.mainloop()
