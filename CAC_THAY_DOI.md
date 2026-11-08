# Các thay đổi đã thực hiện

- Chuẩn hóa tên file Python, requirements và BAT (bỏ hậu tố tải xuống).
- CLI chọn chính xác một checkpoint, không chọn nhầm ensemble; hỗ trợ đủ 4 CNN,
  tìm model theo thư mục mã nguồn và xử lý xoay EXIF.
- Thông báo thiếu thư viện dẫn tới bộ cài BAT có thật, không yêu cầu requirements_cnn.txt.
- Thống nhất chân trang thành UNETI12 · AIX.
- Tóm tắt metrics đọc thêm final_val_macro_f1/final_val_accuracy.
- Bootstrap mặc định 800 lần; thêm --bootstrap-iterations và lưu số lần/seed vào JSON.
  Không tự sửa số CI cũ; README phân biệt số liệu lịch sử chưa được kiểm chứng lại.
- Cache CNN được làm mới khi dung lượng hoặc mtime checkpoint thay đổi.
- Chẩn đoán thử import thật, liệt kê đúng checkpoint được hỗ trợ và kiểm tra src.predict
  khi có model truyền thống; báo riêng thiếu module cần cho huấn luyện.
- Thêm BAT cài thư viện và kiểm tra, .gitignore, công cụ tìm file lớn khi tải GitHub.
- Không thay đổi trọng số hoặc kết quả thực nghiệm; không tạo src hay checkpoint giả.

## Kiểm tra

Toàn bộ Python đã qua kiểm tra cú pháp; 5 bài kiểm tra hồi quy đạt:
chọn MobileNet khi có ensemble; hiển thị metrics CNN; tổng hợp và giới hạn đa góc;
quy tắc tư vấn/CSV; bootstrap ghi số vòng và từ chối tập validation không khớp.
Kiểm tra CLI dùng bộ suy luận giả lập chỉ trong test, không chứng minh mô hình thật.
Chưa chạy Streamlit trên Windows hoặc nạp checkpoint vì các đầu vào đó chưa được gửi.

## Cách áp dụng

Chép nội dung gói này vào dự án cũ chứa app.py, giữ nguyên model/, src/, results/,
results_cnn/. Sau khi thay file, dừng web cũ rồi chạy lại BAT.
