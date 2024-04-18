## Cách sử dụng:

1. Khởi động các services bằng lệnh:
```
docker compose up
```

2. Cài đặt thư viện cần thiết bằng pip:
```
pip install kafka-python
```

3. Di chuyển đến thư mục `kafka_python`:
```
cd kafka_python
```

4. Tạo topic với cấu hình cho tin nhắn:
```
python3 management.py
```

5. Đăng tin nhắn lên topic:
```
python3 producers.py
```

6. Đăng ký nhận tin nhắn từ topic:
```
python3 consumers.py
```

- File `consumers.py` sẽ lưu các frame hình ảnh được nhận vào thư mục `image`.

## Ghi chú quan trọng:

- Để chỉnh sửa topic và cài đặt tự động xóa tin nhắn sau 1 phút, sử dụng lệnh sau:
```bash
kafka-topics.sh --alter --topic streaming --config retention.ms=60000 --zookeeper zookeeper:2181
```

- Để đặt thời gian sống cho tin nhắn trên Kafka hoặc xóa tin nhắn sau khi một số lượng nhất định tin nhắn đã được sản xuất đến một partition, bạn có thể sử dụng cấu hình `retention.ms` và `retention.bytes` cho topic Kafka của bạn.

- Cấu hình `retention.ms` xác định thời gian tối đa mà một tin nhắn được giữ lại trước khi bị xóa. Ví dụ, nếu bạn đặt `retention.ms` là `86400000` (1 ngày), bất kỳ tin nhắn nào cũ hơn 1 ngày sẽ được xóa.

- Cấu hình `retention.bytes` xác định lượng dữ liệu tối đa được giữ lại trước khi tin nhắn được xóa. Ví dụ, nếu bạn đặt retention.bytes là 1073741824 (1 GB), bất kỳ tin nhắn nào vượt quá tổng cỡ 1 GB sẽ bị xóa.

- Bạn có thể đặt những cấu hình này khi tạo một topic mới hoặc chỉnh sửa topic hiện có bằng công cụ dòng lệnh `kafka-topics`. Ví dụ, để tạo một topic mới với thời gian giữ tin nhắn là 1 ngày và cỡ tối đa là 1 GB, bạn có thể sử dụng lệnh sau:
```bash
kafka-topics.sh --create --topic my-topic --replication-factor 1 --partitions 1 --config retention.ms=86400000 --config retention.bytes=1073741824
```
## Liên kết tham khảo:
https://github.com/better-data-science/Apache-Kafka-in-Python
https://betterdatascience.com/how-to-install-apache-kafka-using-docker-the-easy-way/
https://betterdatascience.com/master-the-kafka-shell-in-5-minutes-topics-producers-and-consumers-explained/
https://github.com/segmentio/kafka-go