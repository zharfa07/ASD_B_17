# riwayat.py
from update import stack_update

def tampilkan_riwayat():

    print("\n=== Riwayat Update ===")

    if not stack_update:
        print("Belum ada riwayat.")

    else:
        for item in reversed(stack_update):
            print(item)
