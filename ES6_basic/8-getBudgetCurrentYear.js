// This function uses ES6 computed property names to dynamically
// build object keys based on the current year.
function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const budget = {

  [`income-${getCurrentYear()}`]: income,
	[`gdp-${getCurrentYear()}`]: gdp,
  [`capita-${getCurrentYear()}`]: capita,
	};
  return budget;
}
