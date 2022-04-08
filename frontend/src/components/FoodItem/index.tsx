import React from 'react';

import { Food } from '../../store/ducks/foods/types';

interface OwnProps {
  food: Food;
}

export default ({ food }: OwnProps) => (
  <tr key={food.id}>
    <td>{food.name}</td>
    <td>{food.quantity}</td>
    <td>{food.proteins}</td>
    <td>{food.carbohydrates}</td>
    <td>{food.fats}</td>
  </tr>
);
