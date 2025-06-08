# ReactKickstart 🚀

**Modern, Kapsamlı ve Üretime Hazır React Başlangıç Şablonu (Boilerplate)**

<p align="center">
  <img src="https://raw.githubusercontent.com/reactkick/ReactKickstart/main/.github/logo.png" alt="ReactKickstart Logo" width="150"/>
</p>

<p align="center">
  <!-- Projeniz için uygun olanları ekleyebilirsiniz -->
  <a href="https://github.com/reactkick/ReactKickstart/actions"><img src="https://img.shields.io/github/actions/workflow/status/reactkick/ReactKickstart/main.yml?branch=main&style=for-the-badge" alt="Build Status"></a>
  <a href="https://github.com/reactkick/ReactKickstart/blob/main/LICENSE"><img src="https://img.shields.io/github/license/reactkick/ReactKickstart?style=for-the-badge" alt="License"></a>
  <a href="https://github.com/reactkick/ReactKickstart/pulls"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=for-the-badge" alt="PRs Welcome"></a>
</p>

**ReactKickstart**, modern web uygulamaları geliştirmeye ışık hızında başlamanızı sağlamak için tasarlanmış bir başlangıç kitidir. TypeScript, Redux Toolkit, Styled Components ve React Router gibi endüstri standardı araçlarla önceden yapılandırılmıştır. Amacımız, proje kurulumu ve yapılandırma zahmetinden kurtulmanızı sağlayarak doğrudan harika özellikler oluşturmaya odaklanmanıza olanak tanımaktır.

## ✨ Ana Özellikler

- **⚡️ Modern Teknoloji Yığını:** React 18, TypeScript ve CRA (Create React App) üzerine kurulmuştur.
- **💅 Dinamik Stil Yönetimi:** `Styled Components` ile komponent bazlı, izole ve dinamik stilizasyon. Tema desteği mevcuttur.
- **📦 Verimli State Yönetimi:** `Redux Toolkit` ile öngörülebilir, basit ve güçlü state yönetimi.
- **🧭 Akıllı Yönlendirme:** `React Router v6` ile modern, dinamik ve iç içe yönlendirme (routing) çözümleri.
- **✅ Kod Kalitesi:** `ESLint` ve `Prettier` ile kod standartları ve formatlama otomatik olarak sağlanır.
- **📁 Mantıksal Klasör Yapısı:** Ölçeklenebilir ve bakımı kolay uygulamalar için tasarlanmış sezgisel bir klasör yapısı.
- **🌐 API İstekleri:** `axios` ile API istekleri için hazır yapılandırma.

## 🏁 Hızlı Başlangıç

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları izleyin.

### Ön Gereksinimler

Başlamadan önce sisteminizde aşağıdaki araçların kurulu olduğundan emin olun:
- [Node.js](https://nodejs.org/) (v16 veya üstü önerilir)
- [Git](https://git-scm.com/)
- `npm` veya `yarn` paket yöneticisi

### Kurulum

1.  **Projeyi klonlayın:**
    ```bash
    git clone https://github.com/reactkick/ReactKickstart.git
    ```

2.  **Proje dizinine gidin:**
    ```bash
    cd ReactKickstart
    ```

3.  **Gerekli paketleri yükleyin:**

    `npm` ile:
    ```bash
    npm install
    ```
    veya `yarn` ile:
    ```bash
    yarn install
    ```

4.  **Geliştirme sunucusunu başlatın:**

    `npm` ile:
    ```bash
    npm start
    ```
    veya `yarn` ile:
    ```bash
    yarn start
    ```

Uygulamanız artık tarayıcıda `http://localhost:3000` adresinde çalışıyor olmalı!

## 📜 Kullanılabilir Komutlar

- `npm start`: Geliştirme modunda uygulamayı başlatır.
- `npm run build`: Uygulamayı üretim için `build` klasörüne paketler.
- `npm test`: Testleri interaktif izleme modunda çalıştırır.
- `npm run lint`: ESLint ile kod dosyalarındaki hataları denetler.
- `npm run format`: Prettier ile tüm kod dosyalarını formatlar.

## 📁 Klasör Yapısı

Proje, ölçeklenebilirliği göz önünde bulundurarak mantıksal bir klasör yapısı kullanır:

```
src
├── api/          # Axios instance ve API çağrı fonksiyonları
├── assets/       # Resimler, fontlar gibi statik varlıklar
├── components/   # Yeniden kullanılabilir UI komponentleri (Button, Input, vb.)
├── hooks/        # Özel (custom) React hook'ları
├── pages/        # Sayfa seviyesindeki ana komponentler (HomePage, AboutPage, vb.)
├── store/        # Redux Toolkit state yönetimi
│   ├── slices/   # Her bir state dilimi (slice) burada tanımlanır
│   └── store.ts  # Redux store'un yapılandırıldığı yer
├── styles/       # Global stiller ve tema dosyaları (theme.ts)
├── types/        # Global TypeScript tipleri ve arayüzleri
├── utils/        # Yardımcı fonksiyonlar
├── App.tsx       # Ana uygulama komponenti, yönlendirme mantığını içerir
├── index.tsx     # Uygulamanın giriş noktası (DOM render)
└── react-app-env.d.ts
```

## (Core Concepts)

### Stil Yönetimi (Styled Components)

Komponentlerinizi stilize etmek için `styled-components` kullanıyoruz. Global tema ayarları `src/styles/theme.ts` dosyasında bulunur. Komponentlerinizde bu temayı kolayca kullanabilirsiniz.

**Örnek:**
```tsx
import styled from 'styled-components';

const PrimaryButton = styled.button`
  background-color: ${props => props.theme.colors.primary};
  color: ${props => props.theme.colors.white};
  padding: 10px 20px;
  border: none;
  border-radius: ${props => props.theme.borderRadius};
  cursor: pointer;

  &:hover {
    opacity: 0.9;
  }
`;
```

### State Yönetimi (Redux Toolkit)

Uygulama genelindeki state'leri yönetmek için Redux Toolkit'in "slice" modelini kullanıyoruz. Yeni bir state dilimi eklemek için:

1.  `src/store/slices/` klasöründe `myFeatureSlice.ts` gibi yeni bir dosya oluşturun.
2.  `createSlice` kullanarak slice'ınızı tanımlayın.
3.  Oluşturduğunuz reducer'ı `src/store/store.ts` dosyasında store'a ekleyin.

Komponentlerinizde state'e erişmek için `useSelector`, action'ları tetiklemek için `useDispatch` hook'larını kullanın.

## 🤝 Katkıda Bulunma

Katkılarınız projeyi daha iyi hale getirecektir! Lütfen katkıda bulunmaktan çekinmeyin.

1.  Projeyi **Fork**'layın.
2.  Yeni bir özellik veya hata düzeltmesi için yeni bir **Branch** oluşturun (`git checkout -b feature/yeni-ozellik` veya `git checkout -b fix/hata-duzeltmesi`).
3.  Değişikliklerinizi yapın ve **Commit**'leyin.
4.  Değişikliklerinizi kendi Fork'unuza **Push**'layın.
5.  Bir **Pull Request** açın ve yaptığınız değişiklikleri detaylı bir şekilde açıklayın.

Hata bildirimleri ve özellik talepleri için lütfen [GitHub Issues](https://github.com/reactkick/ReactKickstart/issues) bölümünü kullanın.

## 📄 Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Detaylar için [LICENSE](LICENSE) dosyasına göz atın.
