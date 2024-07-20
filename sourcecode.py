import json

# Data pengguna (simulasi database)
users = {
    "user1": {"name": "John Doe", "age": 30, "email": "john.doe@example.com"},
    "user2": {"name": "Jane Smith", "age": 25, "email": "jane.smith@example.com"}
}

def display_menu():
    print("\nMenu:")
    print("1. Tampilkan Data Pengguna")
    print("2. Tambah Pengguna")
    print("3. Hapus Pengguna")
    print("4. Kalkulator")
    print("5. Simpan Data ke File")
    print("6. Muat Data dari File")
    print("7. Keluar")

def show_users():
    print("\nDaftar Pengguna:")
    for username, data in users.items():
        print(f"Username: {username}")
        print(f"Nama: {data['name']}")
        print(f"Usia: {data['age']}")
        print(f"Email: {data['email']}\n")

def add_user():
    username = input("\nMasukkan username baru: ")
    if username in users:
        print("Username sudah ada!")
        return
    name = input("Masukkan nama: ")
    age = int(input("Masukkan usia: "))
    email = input("Masukkan email: ")
    users[username] = {"name": name, "age": age, "email": email}
    print("Pengguna ditambahkan!")

def delete_user():
    username = input("\nMasukkan username yang ingin dihapus: ")
    if username in users:
        del users[username]
        print("Pengguna dihapus!")
    else:
        print("Username tidak ditemukan!")

def calculator():
    print("\nKalkulator Sederhana")
    print("Operasi yang tersedia: +, -, *, /")
    operation = input("Masukkan operasi: ")
    try:
        num1 = float(input("Masukkan angka pertama: "))
        num2 = float(input("Masukkan angka kedua: "))
        
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Pembagian dengan nol!")
                return
            result = num1 / num2
        else:
            print("Operasi tidak dikenali!")
            return
        
        print(f"Hasil: {result}")
    except ValueError:
        print("Error: Masukkan angka yang valid!")

def save_to_file():
    with open("users_data.json", "w") as file:
        json.dump(users, file, indent=4)
    print("Data pengguna disimpan ke file!")

def load_from_file():
    global users
    try:
        with open("users_data.json", "r") as file:
            users = json.load(file)
        print("Data pengguna dimuat dari file!")
    except FileNotFoundError:
        print("File tidak ditemukan!")

def main():
    while True:
        display_menu()
        choice = input("\nPilih menu (1-7): ")

        if choice == '1':
            show_users()
        elif choice == '2':
            add_user()
        elif choice == '3':
            delete_user()
        elif choice == '4':
            calculator()
        elif choice == '5':
            save_to_file()
        elif choice == '6':
            load_from_file()
        elif choice == '7':
            print("Keluar dari aplikasi...")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
