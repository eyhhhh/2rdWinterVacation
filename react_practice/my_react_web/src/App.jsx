import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from './pages/Home';
import Gugudan from './pages/Gugudan';
import CourseCardPage from './pages/CourseCard';
import AccordionPage from './pages/Accordion';
import SurveyPage from './pages/Survey';

const App = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/gugudan" element={<Gugudan />} />
        <Route path="/coursecard" element={<CourseCardPage />} />
        <Route path="/accordion" element={<AccordionPage />} />
        <Route path="/survey" element={<SurveyPage />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;