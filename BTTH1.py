initial_total_amount = int(input("Nhập tổng tiền hóa đơn ban đầu: "))
print("--- HÓA ĐƠN THANH TOÁN RIKKEI STORE ---")
if initial_total_amount >= 500000:
    discount = initial_total_amount * 0.1
else:    
    discount = initial_total_amount
print(f"Số tiền được giảm giá: {discount} VND")
final_total_amount = initial_total_amount - discount
print(f"Tổng tiền khách phải trả: {final_total_amount} VND")