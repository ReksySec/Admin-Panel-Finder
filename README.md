# Brute Force İle Detaylı Admin Panel Bulucu

Ben Reksy,

Bu proje, bir web sitesinde yönetici giriş sayfalarını bulmak için geliştirilmiş bir brute-force tarayıcısını içerir. Bu Python kodu, belirli yolları deneyerek admin paneli bulmaya yönelik tasarlanmıştır. İşte projenin detaylı açıklaması:

## Proje Açıklaması

Bu Python kodu, aşağıdaki işlevleri yerine getirir:

1. **Admin Paneli Bulma**: Kod, çeşitli admin yollarını test ederek hedef web sitesinde admin giriş sayfalarını bulur. Kullanıcıdan alınan URL üzerinde çeşitli yolları denemek suretiyle, admin giriş sayfalarını tespit etmeye çalışır.

2. **Çıktı Dosyası**: Bulunan admin giriş sayfalarının URL'leri, masaüstünüzde `admins.txt` dosyasına kaydedilir. Bu dosya, tarama sonuçlarını saklamak ve daha fazla analiz yapmak için kullanılır.

3. **Kullanım Sonrası**: Tarayıcı tarafından bulunan admin giriş sayfalarını nasıl kullanabileceğiniz hakkında bilgi vermekte fayda var. Etik ve yasal sınırlar içinde kalmanız önemlidir. Web güvenliği testleri yaparken, genellikle izin alınması gerektiğini unutmayın.

## Kurulum ve Kullanım

1. **Gerekli Kütüphaneler**: Proje, `requests`, `random`, `logging`, `os` ve `tqdm` kütüphanelerini kullanır. Bu kütüphaneleri yüklemek için terminalde aşağıdaki komutu çalıştırabilirsiniz:

   ```bash
   pip install requests tqdm
