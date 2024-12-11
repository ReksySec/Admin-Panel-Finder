# Reksy Admin Panel Finder  

**Reksy Admin Panel Finder**, brute-force yöntemiyle bir web sitesindeki yönetici giriş sayfalarını bulmak için geliştirilmiş güçlü bir Python aracıdır. Bu araç, hedef URL üzerinde belirli yolları dener ve yönetici giriş noktalarını tespit ederek çıktı dosyasına kaydeder.  

## 🚀 Özellikler  
- **Admin Panel Bulucu**:  
  Belirli yolları brute-force yöntemiyle tarayarak hedef sitenin admin giriş sayfalarını bulur.  
- **Sonuçların Kaydedilmesi**:  
  Bulunan admin panelleri, masaüstünüzde otomatik olarak `admins.txt` adlı bir dosyaya kaydedilir.  
- **Kullanıcı Dostu**:  
  Kolay kullanım için tasarlanmış, kullanıcıdan yalnızca URL girmesi beklenir.  

## 🛠️ Gereksinimler  
Bu aracı kullanabilmek için aşağıdaki Python kütüphanelerine ihtiyaç vardır:  
- `requests`: HTTP isteklerini gerçekleştirmek için.  
- `tqdm`: Tarama ilerleme çubuğunu göstermek için.  
- `os`, `logging`, `random`: Python standart kütüphaneleri.  

Kurulum için şu komutu çalıştırabilirsiniz:  
```bash
pip install requests tqdm
```
📖 Kullanım
Kodun Çalıştırılması

Python dosyasını indirin ve çalıştırın:
```
python reksy_admin_finder.py
```

Kullanıcıdan istenen URL'yi girin.

Sonuçların Kaydedilmesi

Tarama sonuçları, masaüstünüzde admins.txt dosyasına kaydedilecektir.

Yasal Kullanım Uyarısı

Bu araç, yalnızca izinli güvenlik testleri için kullanılmalıdır.

Her zaman etik ve yasal sınırlar içinde hareket ettiğinizden emin olun.

🔍 Projenin Teknik Detayları

Admin Panel Paths: Araç, yaygın olarak kullanılan admin panel yollarını dener.

Çıkış Dosyası: Tespit edilen giriş sayfaları, yeniden kullanım veya analiz için admins.txt dosyasına kaydedilir.

🌟 Katkıda Bulunun

Proje hakkında geri bildirimde bulunmak veya katkıda bulunmak için GitHub üzerinden benimle iletişime geçebilirsiniz.
