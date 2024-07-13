from jinja2 import Template

slice_template = Template('''

import { createSlice, PayloadAction } from '@reduxjs/toolkit'
import { RootState } from '../store/rootReducer'

export const counterSlice = createSlice({
  name: 'counter',
  initialState: {
    value: 0,
  },
  reducers: {
    increment: (state) => {
      state.value += 1;
    },
    decrement: (state) => {
      state.value -= 1;
    },
    incrementByAmount: (state, action: PayloadAction<number>) => {
      state.value += action.payload;
    },
  },
})

export const { increment, decrement, incrementByAmount } = counterSlice.actions

export const selectCounterValue = (state: RootState) => state.counter.value

export default counterSlice.reducer''')