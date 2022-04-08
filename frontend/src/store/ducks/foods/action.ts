import { FoodsTypes, Food } from './types';

export const loadRequest = () => ({
  type: FoodsTypes.LOAD_REQUEST,
});

export const loadSuccess = (data: Food[]) => ({
  type: FoodsTypes.LOAD_SUCCESS,
  payload: { data },
});

export const loadFailure = () => ({
  type: FoodsTypes.LOAD_FAILURE,
});
