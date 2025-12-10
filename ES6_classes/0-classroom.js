// Define a class named ClassRoom
export default class ClassRoom{
	constructor(maxStudentsSize) {
		this._maxStudentsSize = maxStudentsSize;
	}
	get maxStudentsSize() {
		return this._maxStudentsSize;
	}
}
