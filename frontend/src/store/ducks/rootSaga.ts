import { all, takeLatest, StrictEffect } from 'redux-saga/effects';

import { FoodsTypes } from './foods/types';
import { load } from './foods/saga';

export default function* rootSaga(): Generator<StrictEffect> {
  return yield all([takeLatest(FoodsTypes.LOAD_REQUEST, load)]);
}
