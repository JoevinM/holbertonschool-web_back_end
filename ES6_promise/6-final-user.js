import signUpUser from "./4-user-promise";
import uploadPhoto from "./5-photo-reject";

export default function handleProfileSignup(firstName, lastName, fileName) {
	if (typeof firstName !== 'string'
		|| typeof lastName !== 'string'
		|| typeof fileName !== 'string') {
			throw new TypeError('Arguments must be strings');
		}
	return Promise.allSettled([
		signUpUser(firstName, lastName),
		uploadPhoto(fileName),
	]);
}
