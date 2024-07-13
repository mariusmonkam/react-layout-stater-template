from jinja2 import Template

counter_template = Template('''
import React from 'react'
import { useSelector } from 'react-redux'
import { increment, decrement, incrementByAmount, selectCounterValue } from '../features/counterSlice'
import { useAppDispatch } from '../store/store'

const Counter: React.FC = () => {
  const count = useSelector(selectCounterValue)
  const dispatch = useAppDispatch()

  return (
    <div>
      <h1>Counter</h1>
      <p>{count}</p>
      <button onClick={() => dispatch(increment())}>Increment</button>
      <button onClick={() => dispatch(decrement())}>Decrement</button>
      <button onClick={() => dispatch(incrementByAmount(2))}>Increment by 2</button>
    </div>
  )
}

export default Counter;
''')