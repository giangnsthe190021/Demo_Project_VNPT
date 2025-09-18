# User & Course Management System

## Giới thiệu
Dự án này được xây dựng nhằm hỗ trợ **quản trị người dùng và khóa học** trong một hệ thống học tập số.  
Chương trình cho phép quản lý tài khoản, phân quyền truy cập, và đặc biệt là khả năng **tạo thẻ nhớ (flashcards) và quiz ôn tập** trực tiếp từ file Word (DOCX).  
Mục tiêu của dự án là tự động hóa quy trình dạy - học, giúp việc ôn tập trở nên trực quan và hiệu quả hơn.

---

## Nguyên lý hoạt động

1. **Quản lý người dùng & phân quyền**  
   - Admin có thể tạo tài khoản mới, chỉnh sửa thông tin người dùng hoặc phân quyền truy cập.  
   - Hệ thống xác thực người dùng khi đăng nhập để đảm bảo an toàn.  

2. **Tạo và quản lý khóa học**  
   - Người dùng được cấp quyền có thể tạo khóa học mới.  
   - Mỗi khóa học bao gồm thông tin mô tả, nội dung giảng dạy, và tài liệu liên quan.  

3. **Xử lý file Word để sinh Quiz & Flashcards**  
   - Người quản trị hoặc giảng viên tải lên tài liệu giảng dạy dưới dạng file Word (.docx).  
   - Hệ thống sẽ tự động phân tích nội dung file, trích xuất câu hỏi và đáp án.  
   - Từ dữ liệu này, chương trình tạo ra:  
     - **Quiz trắc nghiệm** để kiểm tra kiến thức.  
     - **Flashcards** phục vụ ôn tập nhanh.  

4. **Lưu trữ dữ liệu**  
   - Dữ liệu người dùng, khóa học, quiz và flashcards được lưu trong cơ sở dữ liệu của ứng dụng (hoặc file `.sqlite3` mặc định trong Django).  
   - Các tệp tài liệu (file Word, hình ảnh, media) được lưu trong thư mục `media/`.  

5. **Triển khai & mở rộng**  
   - Hệ thống có thể được triển khai trên máy chủ hoặc đẩy lên GitHub để cộng tác phát triển.  
   - Cấu trúc được thiết kế theo mô hình **Django MVC (Model - View - Controller)**, dễ bảo trì và mở rộng trong tương lai.  

---

## Tính năng chính
- Quản lý người dùng, đăng ký, đăng nhập, phân quyền.  
- Tạo và chỉnh sửa khóa học.  
- Tự động sinh quiz & flashcards từ tài liệu Word.  
- Lưu trữ dữ liệu an toàn trong cơ sở dữ liệu.  
- Giao diện web trực quan, dễ sử dụng.  

---

## Hướng phát triển
- Tích hợp API để cho phép import dữ liệu từ nhiều định dạng khác nhau.  
- Phát triển tính năng học nhóm và thống kê kết quả học tập.  
- Tích hợp trí tuệ nhân tạo để sinh câu hỏi ôn tập thông minh hơn.  




## Hướng dẫn sử dụng: ##
Hiện tại có các tài khoản:

+) Admin_User: (Có thể truy cập vào các Courses đã tạo, xem thông tin và cập nhật thông tin người dùng ) 
- User: Giang_Admin
- pass: Tham091105$

+) Admin tạo course ( đây là admin các courses đã tạo, người dùng nào cũng có thể tự tạo courses riêng của mình )
- User: Songiang
- pass: 12345

+) User + passwords ( Các người dùng đã được tạo sẵn và thêm vào khóa học ) 
1. - Hoang ( Truy cập được các courses ) 
   - 12345
     
2. - Hung ( Truy cập được các courses )
   - 12345
     
3. - Dung ( Người dùng đã được thêm vào 1 course duy nhất và các course khác sẽ không vào được )
   - 12345
  
+) Admin tổng có thể xóa được dữ liệu người dùng ( vào bằng thêm đuôi "http://127.0.0.1:8000/admin/ )
- User: giang
- pass: 12345


## Các chức năng của web ##
- Tạo người dùng
- Tạo khóa học
- Thêm dữ liệu khóa học từ file docs
- Chuyển dữ liệu từ file docs sang quizz và flasscards để ôn tập
- Xem nội dung trực tiếp file docs
- Thêm người dùng vào khóa học
- Xóa khóa học
- Cập nhật thông tin người dùng ( Tên, SDT, Gmail, Địa chỉ nhà, Ghi chú, Ảnh đại diện)

Khi muốn chạy:
- **cd** đến thư mục **myproject** ( "cd .\Demo_Project_VNPT-main\project1_newweb\myproject\" )
- Dùng lệnh **python manage.py runserver**
- cài python-docx nếu cần 
