/**
 * Action Types
 */
// eslint-disable-next-line no-shadow
export enum FoodsTypes {
  LOAD_REQUEST = '@foods/LOAD_REQUEST',
  LOAD_SUCCESS = '@foods/LOAD_SUCCESS',
  LOAD_FAILURE = '@foods/LOAD_FAILURE',
}

export interface FoodQueryFilter {
  greatest: `calories` | `carbohydrates` | `proteins` | `fats`;
}

export interface GetFoodAction {
  type: FoodsTypes.LOAD_REQUEST;
  filters: FoodQueryFilter;
}

/**
 * Data Types
 */
export interface Food {
  id: number;
  name: string;
  quantity: number;
  proteins: number;
  carbohydrates: number;
  fats: number;
}

/**
 * State Types
 */
export interface FoodsState {
  readonly data: Food[];
  readonly loading: boolean;
  readonly error: boolean;
}
