import React from 'react';
import FoodList from '../../components/FoodList';

const ProteinsPage = () => (
  <FoodList
    title="Alimentos com mais proteínas"
    filters={{
      greatest: 'proteins',
    }}
  />
);

export default ProteinsPage;
