import { call, put } from 'redux-saga/effects';
import { AxiosResponse } from 'axios';
import api from '../../../services/api';
import { loadFailure, loadSuccess } from './action';
import { Food } from './types';

export function* load() {
  try {
    const response: AxiosResponse<Food[]> = yield call(api.get, '/foods');

    yield put(loadSuccess(response.data));
  } catch (err) {
    yield put(loadFailure());
  }
}
