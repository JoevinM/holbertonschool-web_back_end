// This function illustrates block scoping in ES6:
// variables declared with const inside the conditional block
// do not overwrite variables declared with var in the outer function scope.
export default function taskBlock(trueOrFalse) {
  var task = false;
  var task2 = true;

  if (trueOrFalse) {
    const task = true;
    const task2 = false;
  }

  return [task, task2];
}
