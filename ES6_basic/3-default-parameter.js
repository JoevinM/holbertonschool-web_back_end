// This function uses ES6 default parameters to assign fallback values
// when optional arguments are not provided.
export default function getSumOfHoods(initialNumber, expansion1989 = 89, expansion2019 = 19) {
  return initialNumber + expansion1989 + expansion2019;
}
