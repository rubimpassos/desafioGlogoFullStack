import React from 'react';
import { Provider } from 'react-redux';

import './App.css';
import FoodList from './components/FoodList';

import store from './store';

const App = () => (
  <div className="App">
    <header className="App-header">
      <p>
        Edit <code>src/App.tsx</code> and save to reload.
      </p>
      <a
        className="App-link"
        href="https://reactjs.org"
        target="_blank"
        rel="noopener noreferrer"
      >
        Learn React
      </a>
    </header>
    <Provider store={store}>
      <FoodList />
    </Provider>
  </div>
);

export default App;
