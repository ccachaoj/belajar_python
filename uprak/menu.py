# Daftar harga coffee
harga_coffee = {
    "caffe americano": 37000,
    "caramel macchiato": 59000,
    "asian dolce latte": 55000,
    "caramel latte": 52000,
    "vanilla latte": 52000,
    "caffe latte": 48000,
    "cappuccino": 48000,
    "caffe mocha": 55000
}

# Input pesanan
pesanan = {}
subtotal = 0

while True:
    print("\nSelamat datang, selamat berbelanja")
    print("Berikut adalah daftar barang yang tersedia:")
    for k, v in harga_coffee.items():
        print(f"{k}: {v} per cup")

    item = input("Masukkan pesanan anda (atau 'order' untuk selesai): ").lower()
    if item == "order":
        break

    if item in harga_coffee:
        jumlah = int(input(f"Berapa cup {item} yang anda inginkan? "))
        pesanan[item] = jumlah
        subtotal += harga_coffee[item] * jumlah

# Hitung total belanja
ppn = subtotal * 0.1
total_bayar = subtotal + ppn

if subtotal > 350000:
    diskon = total_bayar * 0.15
    total_bayar -= diskon

# Output total belanja
print("\nTotal belanja anda adalah: Rp{:,.0f}".format(subtotal))
print("PPN 10 %: Rp{:,.0f}".format(ppn))
print("Diskon 15 %: Rp{:,.0f}".format(diskon if diskon > 0 else 0))
print("Total belanja anda setelah pajak dan diskon: Rp{:,.0f}".format(total_bayar))