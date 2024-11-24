import random
aa = ['VÕ HOÀI AN','BÙI HẢI ANH','LÊ PHẠM QUỲNH ANH','NGUYỄN HẢI ANH','NGUYỄN PHƯƠNG ANH 5','NGUYỄN PHƯƠNG ANH 6','NGUYỄN ĐẶNG MINH CHIẾN','BÙI QUANG DŨNG','ĐÀM VĂN DŨNG','ĐÀO KHÁNH DUY','ĐOÀN PHƯƠNG DƯƠNG','NGUYỄN ĐỨC ĐẠO','NGUYỄN HẢI HÀ','NGUYỄN ĐĂNG HOÀNG HẢI','NGUYỄN ĐẶNG GIA HIỂN','VŨ ĐẠI HIỆP','ĐẶNG TRẦN TRUNG HIẾU','LÊ ĐÌNH HIẾU','NGUYỄN QUANG HUY','TRỊNH QUANG HUY','VŨ GIA HUY','ĐẶNG THANH HƯƠNG','NGUYỄN ĐỨC GIA KHÁNH','NGUYỄN GIA KHÁNH','NGUYỄN NAM KHÁNH','NGÔ MINH KHUÊ','DƯƠNG MẠNH LÂN','NGUYỄN THỊ TRANG LINH','NGUYỄN ĐẠO BẢO LONG','NGUYỄN ĐÌNH MINH LƯỢNG','PHẠM THỊ QUỲNH MAI','VŨ HOÀNG NHẬT MINH','TÔ HOÀNG NAM','NGUYẾN TIẾN NGHĨA','NGUYỄN QUANG PHƯƠNG','NGUYỄN MINH QUANG','LƯƠNG THÁI SƠN','ĐẶNG NGUYỄN ĐỨC THẮNG','TRINH XUÂN THUẬN','PHẠM ĐỨC TOÀN','NGUYỄN HOÀNG THU TRANG','NGUYỄN THỊ QUỲNH TRÂM','LÊ TÚ UYÊN','NGUYỄN TIẾN VĂN']
pairs = {}
for p in range(len(aa) // 2):
    pairs[p+1] = ( aa.pop(random.randrange(len(aa))),
        aa.pop(random.randrange(len(aa))) )
print(pairs)