import React from 'react';
import FoodList from '../../components/FoodList';

const App = () => (
  <FoodList
    title="Alimentos com mais carboidratos"
    filters={{
      greatest: 'carbohydrates',
    }}
  />
);

export default App;
