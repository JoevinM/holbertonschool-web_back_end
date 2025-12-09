// This module demonstrates the proper use of const and let in ES6:
// const is used when a variable should not be reassigned,
// while let is used when the variable value needs to change.
export function taskFirst() {
  const task = 'I prefer const when I can.';
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLast();

  return combination;
}
