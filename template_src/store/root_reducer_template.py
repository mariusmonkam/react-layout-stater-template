from jinja2 import Template

root_reducer_template = Template('''

import { combineReducers } from '@reduxjs/toolkit'
import counterReducer from '../features/counterSlice'

const rootReducer = combineReducers({
  counter: counterReducer,
})

export type RootState = ReturnType<typeof rootReducer>
export default rootReducer
''')