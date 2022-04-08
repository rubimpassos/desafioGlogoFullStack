import { FoodsTypes, FoodQueryFilter, Food } from './types';

export const loadRequest = (filters?: FoodQueryFilter) => ({
  type: FoodsTypes.LOAD_REQUEST,
  filters,
});

export const loadSuccess = (data: Food[]) => ({
  type: FoodsTypes.LOAD_SUCCESS,
  payload: { data },
});

export const loadFailure = () => ({
  type: FoodsTypes.LOAD_FAILURE,
});
