import React, { useEffect } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators, Dispatch } from 'redux';

import { Food } from '../../store/ducks/foods/types';
import { ApplicationState } from '../../store';

import * as FoodsActions from '../../store/ducks/foods/action';

interface StateProps {
  foods: Food[];
}

interface DispatchProps {
  loadRequest(): void;
}

type Props = StateProps & DispatchProps;

const FoodList: React.FC<Props> = ({ foods, loadRequest }) => {
  useEffect(() => {
    loadRequest();
  }, [loadRequest]);

  return (
    <div>
      <h1>Food List</h1>
      <table>
        <thead>
          <tr>
            <th>Nome</th>
            <th>Quantidade</th>
            <th>Proteínas</th>
            <th>Carboidratos</th>
            <th>Gorduras</th>
          </tr>
        </thead>
        <tbody>
          {foods.map((food) => (
            <tr key={food.id}>
              <td>{food.name}</td>
              <td>{food.quantity}</td>
              <td>{food.proteins}</td>
              <td>{food.carbohydrates}</td>
              <td>{food.fats}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

const mapStateToProps = (state: ApplicationState) => ({
  foods: state.foods.data,
});

const mapDispatchToProps = (dispatch: Dispatch): DispatchProps =>
  bindActionCreators(FoodsActions, dispatch);

export default connect(mapStateToProps, mapDispatchToProps)(FoodList);
