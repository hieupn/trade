# 📋 HƯỚNG DẪN DEPLOY BOTEA REAL LÊN VERCEL
## Miễn phí 100% — Chỉ cần 15 phút — Dùng mãi mãi

---

## CẤU TRÚC FILE SAU KHI GIẢI NÉN

```
botea-vercel/
├── vercel.json          ← Cấu hình Vercel
├── requirements.txt     ← Thư viện Python
├── api/
│   ├── ticker.py        ← API lấy giá thật
│   └── klines.py        ← API lấy nến thật
└── public/
    └── index.html       ← Giao diện app
```

---

## BƯỚC 1 — TẠO TÀI KHOẢN GITHUB (nếu chưa có)

1. Vào **github.com** → Sign up
2. Dùng email bất kỳ → tạo xong

---

## BƯỚC 2 — TẠO REPOSITORY TRÊN GITHUB

1. Đăng nhập GitHub
2. Nhấn **"+" → "New repository"**
3. Đặt tên: `botea-real`
4. Chọn **Public**
5. Nhấn **"Create repository"**

---

## BƯỚC 3 — UPLOAD FILE LÊN GITHUB

### Cách đơn giản nhất (kéo thả):

1. Vào repo vừa tạo
2. Nhấn **"uploading an existing file"**
3. **Kéo thả** toàn bộ thư mục `botea-vercel` vào
4. Nhấn **"Commit changes"**

### Hoặc dùng GitHub Desktop:
- Tải **GitHub Desktop** tại desktop.github.com
- Clone repo → copy file vào → Commit → Push

---

## BƯỚC 4 — TẠO TÀI KHOẢN VERCEL

1. Vào **vercel.com**
2. Nhấn **"Sign Up"**
3. Chọn **"Continue with GitHub"** (quan trọng!)
4. Authorize Vercel

---

## BƯỚC 5 — DEPLOY LÊN VERCEL

1. Vào dashboard Vercel
2. Nhấn **"New Project"**
3. Tìm repo `botea-real` → nhấn **"Import"**
4. Vercel tự detect cấu hình
5. Nhấn **"Deploy"**
6. Đợi ~1-2 phút...

✅ **Xong! Vercel sẽ cho bạn link dạng:**
```
https://botea-real.vercel.app
```

---

## BƯỚC 6 — MỞ TRÊN IPHONE

1. Mở Safari trên iPhone
2. Vào link Vercel của bạn (vd: `https://botea-real.vercel.app`)
3. Nhấn **Share → Add to Home Screen**
4. App xuất hiện như app thật trên màn hình!

---

## SAU KHI DEPLOY — CÁCH UPDATE

Khi muốn cập nhật code:
1. Sửa file trên GitHub (nhấn edit)
2. Commit changes
3. Vercel **tự động deploy** trong 1-2 phút

---

## TROUBLESHOOTING

### Lỗi "Function timeout"
→ Binance đôi khi chậm — nhấn Phân Tích lại

### Lỗi "404 Not Found" trên /api/ticker
→ Kiểm tra vercel.json đã upload đúng chưa

### App không load
→ Xóa cache Safari → tải lại

---

## GIỚI HẠN VERCEL MIỄN PHÍ

| Tính năng | Giới hạn Free |
|---|---|
| Bandwidth | 100 GB/tháng |
| API calls | 100,000/tháng |
| Deploy | Không giới hạn |
| Domain | .vercel.app miễn phí |

**→ Hoàn toàn đủ dùng cá nhân!**

---

## LƯU Ý QUAN TRỌNG

⚠️ App phân tích kỹ thuật dựa trên dữ liệu thật
⚠️ Không phải lời khuyên đầu tư
⚠️ Luôn đặt Stop Loss trước khi vào lệnh
⚠️ Chỉ rủi ro 1-2% tài khoản mỗi lệnh
