import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';

import HomePage from './containers/HomePage';
import ProteinsPage from './containers/ProteinsPage';
import FatsPage from './containers/FatsPage';
import CarbsPage from './containers/CarbsPage';

const App = () => (
  <div className="App">
    <nav>
      <ul>
        <li>
          <Link to="/">Home</Link>
        </li>
        <li>
          <Link to="/proteinas">Proteínas</Link>
        </li>
        <li>
          <Link to="/carboidratos">Carboidratos</Link>
        </li>
        <li>
          <Link to="/gorduras">Gorduras</Link>
        </li>
      </ul>
    </nav>
    <Routes>
      <Route path="/" element={<HomePage />} />
      <Route path="/proteinas" element={<ProteinsPage />} />
      <Route path="/carboidratos" element={<CarbsPage />} />
      <Route path="/gorduras" element={<FatsPage />} />
    </Routes>
  </div>
);

export default App;
