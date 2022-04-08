import { Reducer } from 'redux';
import { FoodsState, FoodsTypes } from './types';

const INITIAL_STATE: FoodsState = {
  data: [],
  loading: false,
  error: false,
};

const reducer: Reducer<FoodsState> = (state, action) => {
  if (state === undefined) {
    return INITIAL_STATE;
  }

  switch (action.type) {
    case FoodsTypes.LOAD_REQUEST:
      return { ...state, loading: true };
    case FoodsTypes.LOAD_SUCCESS:
      return { ...state, loading: false, data: action.payload.data };
    case FoodsTypes.LOAD_FAILURE:
      return { ...state, loading: false, error: true };
    default:
      return state;
  }
};

export default reducer;
