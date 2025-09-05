def konversi_suhu(nilai, dari, ke):
    dari = dari.lower()
    ke = ke.lower()

    if dari not in ["c", "f", "k"] or ke not in ["c", "f", "k"]:
        return "Error: Satuan tidak valid. Gunakan 'C', 'F', atau 'K'."

    if dari == "k" and nilai < 0:
        return "Error: Nilai Kelvin tidak boleh negatif."

    if dari == ke:
        return nilai

    if dari == "c":
        c = nilai
    elif dari == "f":
        c = (nilai - 32) * 5/9
    elif dari == "k":
        c = nilai - 273.15

    if ke == "c":
        return c
    elif ke == "f":
        return (c * 9/5) + 32
    elif ke == "k":
        return c + 273.15


from utils import konversi_suhu

print("=== KONVERSI SUHU ===")
try:
    nilai = float(input("Masukkan nilai suhu: "))
    dari = input("Dari satuan (C/F/K): ").strip()
    ke = input("Ke satuan (C/F/K): ").strip()

    hasil = konversi_suhu(nilai, dari, ke)

    if isinstance(hasil, str):
        print(hasil)
    else:
        simbol = {"c": "°C", "f": "°F", "k": "K"}
        print(f"Hasil: {nilai}{simbol[dari.lower()]} = {hasil:.1f}{simbol[ke.lower()]}")
except ValueError:
    print("Error: Nilai suhu harus berupa angka.")