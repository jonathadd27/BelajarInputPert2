print("Program Input Nilai Mahasiswa")
matkul = input("Nama MataKuliah :")
namalengkap = input ("Nama Lengkap :")
nilaikehadiran = float(input("Nilai Kehadiran(20%) :"))
nilaitugas = float(input("Nilai Tugas (25%) :"))
nilaiprojek = float(input("Nilai Project (55%) :"))

nilaitotal = float(0.2 * nilaikehadiran) + (0.25 * nilaitugas) + (0.55 * nilaiprojek)
print(namalengkap, "mendapat nilai total", nilaitotal, "pada mata kuliah", matkul)
