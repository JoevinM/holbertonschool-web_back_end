// This function uses the ES6 rest parameter syntax to collect all arguments
// into an array and return the number of arguments passed.
export default function returnHowManyArguments(...args) {
	return args.length
}
