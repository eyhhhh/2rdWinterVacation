import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div>
      <h1>Home Page</h1>
      <nav>
        <ul>
          <li>
            <Link to="/gugudan">Go to Gugudan Page</Link>
          </li>
          <li>
            <Link to="/coursecard">Go to CourseCard Page</Link>
          </li>
          <li>
            <Link to="/accordion">Go to Accordion Page</Link>
          </li>
          <li>
            <Link to="/survey">Go to Survey Page</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Home;