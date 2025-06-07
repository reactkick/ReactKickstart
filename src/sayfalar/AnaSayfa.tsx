// ... diğer importlar
import Greeting from '../components/Greeting';

const HomePage = () => {
  return (
    <div>
      <h1>Welcome to ReactKickstart</h1>
      <Greeting /> {/* Yeni komponenti burada kullanın */}
    </div>
  );
};

export default HomePage;
