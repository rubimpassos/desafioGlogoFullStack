import React from 'react';
import FoodList from '../../components/FoodList';

const App = () => (
  <FoodList
    title="Alimentos com mais gorduras"
    filters={{
      greatest: 'fats',
    }}
  />
);

export default App;
