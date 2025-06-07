import styled from 'styled-components';

const PrimaryButton = styled.button`
  background-color: ${props => props.theme.colors.primary};
  color: white;
  padding: 10px 20px;
`;
src
├── api/          # Axios instance ve merkezi API çağrı fonksiyonları.
├── assets/       # Resimler, fontlar gibi statik dosyalar.
├── components/   # Uygulama genelinde yeniden kullanılabilir UI bileşenleri (örn. Button, Input).
├── features/     # Belirli bir özelliğe ait tüm dosyalar (bileşenler, hook'lar, servisler).
├── hooks/        # Genel amaçlı özel (custom) React hook'ları.
├── pages/        # Her bir rota (route) için ana sayfa bileşenleri (örn. HomePage).
├── store/        # Redux Toolkit state yönetimi merkezi.
│   ├── slices/   # Her bir state dilimi (slice) burada tanımlanır.
│   └── store.ts  # Redux store'un yapılandırıldığı ve birleştirildiği yer.
├── styles/       # Global stiller, font tanımları ve tema dosyası (theme.ts).
├── types/        # Proje genelinde kullanılacak TypeScript tipleri ve arayüzleri.
├── utils/        # Yardımcı ve genel amaçlı fonksiyonlar (formatters, validators vb.).
├── App.tsx       # Ana uygulama bileşeni, yönlendirme (routing) mantığını içerir.
└── index.tsx     # Uygulamanın giriş noktası (DOM render).
