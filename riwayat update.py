def tampilkan_stack():
    print("\nRiwayat Update (Stack):")

    if not stack_update:
        print("Belum ada update.")

    else:
        for item in reversed(stack_update):
            print(item)
