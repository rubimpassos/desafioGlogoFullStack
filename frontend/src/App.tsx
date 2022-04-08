import React from 'react';
import { Provider } from 'react-redux';

import './App.css';
import FoodList from './components/FoodList';

import store from './store';

const App = () => (
  <div className="App">
    <Provider store={store}>
      <FoodList title="Todos os alimentos" />
      <FoodList
        title="Alimentos com mais proteínas"
        filters={{
          greatest: 'proteins',
        }}
      />
      <FoodList
        title="Alimentos com mais carboidratos"
        filters={{
          greatest: 'carbohydrates',
        }}
      />
      <FoodList
        title="Alimentos com mais gorduras"
        filters={{
          greatest: 'fats',
        }}
      />
    </Provider>
  </div>
);

export default App;
