import React, { useEffect } from 'react';
import { connect } from 'react-redux';
import { bindActionCreators, Dispatch } from 'redux';

import { Food, FoodQueryFilter } from '../../store/ducks/foods/types';
import { ApplicationState } from '../../store';

import * as FoodsActions from '../../store/ducks/foods/action';
import FoodItem from '../FoodItem';

interface StateProps {
  title: string;
  foods: Food[];
  // eslint-disable-next-line react/require-default-props
  filters?: FoodQueryFilter;
}

interface DispatchProps {
  loadRequest(filters?: FoodQueryFilter): void;
}

type Props = StateProps & DispatchProps;

const FoodList: React.FC<Props> = ({ title, foods, filters, loadRequest }) => {
  useEffect(() => {
    loadRequest(filters);
  }, [filters, loadRequest]);

  return (
    <div>
      <h1>{title}</h1>
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
            <FoodItem key={food.id} food={food} />
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
