def tim_so_nho_nhat_va_vi_tri_cua_no(a):
    if not a:
        print("Bạn chưa điền số nào")
        return None

    vi_tri_nho_nhat = 1
    gia_tri_nho_nhat = a[1]

    for i in range(1, len(a)):
        if a[i] < gia_tri_nho_nhat:
            gia_tri_nho_nhat = a[i]
            vi_tri_nho_nhat = i+1

    return gia_tri_nho_nhat, vi_tri_nho_nhat
day_so = input("Nhập dãy số: ").split()
so_nho_nhat, vi_tri_nho_nhat = tim_so_nho_nhat_va_vi_tri_cua_no(day_so)
if so_nho_nhat is not None and vi_tri_nho_nhat is not None:
    print(f"Số nhỏ nhất là {so_nho_nhat} và nằm ở vị trí {vi_tri_nho_nhat}.")
      
 