raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "
menu = '''
===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====
1. Hiển thị chuỗi dữ liệu gốc
2. Chuẩn hóa dữ liệu và in báo cáo
3. Tìm kiếm nhân viên theo mã ID
4. Thoát chương trình

'''
while True: 
    print(menu)
    choice = int(input("Nhập lựa chọn của bạn(1-4): "))
    match choice:
        case 1:
            print(raw_data)
            
        case 2:
            list_employee = raw_data.split("|")
            print(f"Mã nhân viên:{" " * 10}| Họ và tên:{" " * 14}| Số điện thoại:{" " * 15}|  Phòng ban: ")
            for employee in list_employee:
                infor = employee.split(';')
                
                emp_id = infor[0].upper().strip()
                emp_name = infor[1].title().strip()
                emp_phone = infor[2].strip()
                emp_phone = emp_phone.replace("-","")
                emp_department = infor[3].upper().strip()

                if not emp_phone.isdigit():
                    emp_phone = "Invalid Format"
                else:
                    emp_phone = "******" + emp_phone[6:]
                
                print(f"Mã nhân viên: {emp_id:<8} | họ và tên: {emp_name:<13}| số điện thoại: {emp_phone:<14}|  phòng ban: {emp_department}")

            
        case 3:
            search_input = input("Nhập id nhân viên muốn tìm: ").strip().upper()
            is_find = False
            list_employee = raw_data.split("|")
            
            for employee in list_employee:
                infor = employee.split(';')
                
                emp_id = infor[0].upper().strip()
                emp_name = infor[1].title().strip()
                emp_phone = infor[2].strip()
                emp_phone = emp_phone.replace("-","")
                emp_department = infor[3].upper().strip()

                if not emp_phone.isdigit():
                    emp_phone = "Invalid Format"
                else:
                    emp_phone = "******" + emp_phone[6:]
                    
                if search_input == emp_id:
                    print(f"Mã nhân viên: {emp_id}, họ và tên: {emp_name}, số điện thoại: {emp_phone},  phòng ban: {emp_department}")
                    is_find = True
                    break
                
            if is_find == False:
                print("Không tìm thấy nhân viên")
                
        case 4:
            print("Thoát chương trình")
            break
        case _:
            print("Lỗi cú pháp!!!!")

    
            
'''
- input: 
    + các lựa chọn
    + mã emp để tìm kiếm
- output: 
    + chuỗi đầu tiên
    + chuỗi đã chuẩn hóa
    + nhân viên đc tìm kiếm
- các phương thức cần dùng: upper(), replace(), title(), split(), strip(), isdigit()

'''
