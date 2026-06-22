# Custom Exception
class NilaiTidakValidError(Exception):
    pass


# Class Utama
class Mahasiswa:
    def __init__(self, nama):
        self.nama = nama

    def input_nilai(self, nilai):
        if nilai < 0 or nilai > 100:
            raise NilaiTidakValidError(
                "Nilai harus berada di antara 0 sampai 100!"
            )

        print(f"Nilai {nilai} berhasil disimpan.")


# Program Utama
try:
    mhs = Mahasiswa("Bagus")

    nilai = int(input("Masukkan nilai mahasiswa: "))

    mhs.input_nilai(nilai)

except NilaiTidakValidError as e:
    print("Error:", e)

except ValueError:
    print("Input harus berupa angka!")

finally:
    print("Proses pemeriksaan nilai telah selesai dilakukan.")
