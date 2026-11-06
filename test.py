s = input("Ten chu ho: ")
print(s)

so_truoc_str = input("Chi so thang truoc: ")
so_truoc = int(so_truoc_str.split(":")[-1].strip())

so_nay_str = input("Chi so thang nay: ")
so_nay = int(so_nay_str.split(":")[-1].strip())

print(so_nay - so_truoc)