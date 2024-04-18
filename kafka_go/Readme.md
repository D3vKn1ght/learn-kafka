
# Kafka-Go Quickstart
### Bước 1: Cài đặt Go
Đảm bảo rằng bạn đã cài đặt Go trên máy của bạn. Bạn có thể tải Go từ trang web chính thức và làm theo hướng dẫn cài đặt: https://golang.org/

### Bước 2: Cài đặt Kafka
Cần có một phiên bản Kafka đang chạy để code có thể kết nối tới. Bạn có thể tìm hướng dẫn cài đặt Kafka tại đây: https://kafka.apache.org/quickstart

### Bước 3: Thiết lập Kafka
1. Khởi động Zookeeper và Kafka Server.
2. Tạo `topic` mà bạn muốn sử dụng bằng công cụ `kafka-topics.sh` có sẵn trong Kafka.

### Bước 4: Chạy Code

1. Đặt code trên vào một file `.go`, ví dụ `main.go`.
2. Mở terminal hoặc command prompt.
3. Chạy code bằng lệnh:
```shell
go run main.go
```

### Cách hoạt động của code:
- Function `produce` được gọi khi chương trình bắt đầu. Nó sẽ chuyển đổi đối tượng `data` thành JSON và gửi đi như một tin nhắn Kafka.
- Function `consumer` được gọi trong một goroutine riêng biệt. Nó lắng nghe các tin nhắn từ Kafka và xuất chúng vào console.

### Đầu ra mong đợi:
- Khi một tin nhắn được sản xuất, nó sẽ thông báo trong console.
- Khi tin nhắn được tiêu thụ, nó sẽ in ra console thông tin của tin nhắn.

Bạn cần chỉnh sửa `listBrokers` đến địa chỉ của broker Kafka mà bạn có.