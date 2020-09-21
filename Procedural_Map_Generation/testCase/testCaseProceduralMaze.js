//Option 2: mark everything as 0, and then generate a random x, y pair within a certain range as a player origin point and reassign it as 1. roll a rand 4 times and if the first is the highest value plot moving up, second down, third right, fourth left. Do so from the new point and continue until an outer boundary is transitioned to 1. Every nth (20?) new tile assign it to either a 2 (safespot) or a 4 (monster) instead.
//Points of concern: It's still complete random for the maze structure, and I don't want to see a big open space and an exit or a straight shot out of the map. Also if it doesnt iterate enough times before escaping there would be no safe spot or monster. I think this is the better of these two and would work with more definition of what is allowed or disallowed. 
//expounding on 2: origin x and y must be (map size / 4) pushed in at a minimum. 

var mapData = [];

var mapSize = 50;
var mapMargin = mapSize / 3;

var divEl = document.getElementById('table here');
var tableEl = document.createElement('table');
divEl.append(tableEl);

for (let i = 0; i < mapSize; i++) {
	mapData.push([]);
	var rowEl = document.createElement('tr');
	rowEl.setAttribute('id', 'row'+i);
	tableEl.append(rowEl);
	for (let j = 0; j < mapSize; j++) {
		mapData[i].push(0);
		var dataEl = document.createElement('td');
		dataEl.setAttribute('id', 'row'+i+'column'+j);
		dataEl.setAttribute('style','background-color:purple;');
		rowEl.append(dataEl);
	}
}

function generateMap(){

	for (let i = 0; i < mapSize; i++) {
		for (let j = 0; j < mapSize; j++) {
			mapData[i][j] = 0;
			var dataCell = document.getElementById('row'+i+'column'+j);
			dataCell.innerHTML = 0;
			dataCell.setAttribute('style','background-color:purple;');
		}
	}

	var originY = Math.ceil(Math.random()*(mapSize-2*mapMargin)+mapMargin);
	var originX = Math.ceil(Math.random()*(mapSize-2*mapMargin)+mapMargin);

	mapData[originY][originX] = 1;

	curY = originY;
	curX = originX;

	var currentCell = document.getElementById('row'+curY+'column'+curX);
	currentCell.setAttribute('style', 'background-color:yellow;');

	var stepCounter = 0;
	var triedToStep = 0;
	var madeAStep = 0;

	do {
		var upRand = Math.random()*10;
		var downRand = Math.random()*10;
		var rightRand = Math.random()*10;
		var leftRand = Math.random()*10;

		// if (mapData[curY+1][curX] == 1 && mapData[curY][curX-1] == 1 && mapData[curY][curX+1] == 1 && mapData[curY-1][curX] == 1){
		// 	curX+=1;
		// }

		if (upRand > downRand && upRand > rightRand && upRand > leftRand) {
			triedToStep++;
			if (mapData[curY-1][curX] == 0 && (mapData[curY-1][curX+1] != 1 || mapData[curY-1][curX-1] != 1)){
				triedToStep = 0;
				madeAStep++;
				curY-=1;
				var currentCell = document.getElementById('row'+curY+'column'+curX);
				if (madeAStep%120 == 0){
					mapData[curY][curX] = 4;
					currentCell.setAttribute('style', 'background-color:green;');
					currentCell.innerHTML = madeAStep;
				} else if (madeAStep%20 == 0){
					mapData[curY][curX] = 2;
					currentCell.setAttribute('style', 'background-color:blue;');
					currentCell.innerHTML = madeAStep;
				} else {
					mapData[curY][curX] = 1;
					currentCell.setAttribute('style', 'background-color:red;');
					currentCell.innerHTML = madeAStep;
				}
			}
		} else if (downRand > rightRand && downRand > leftRand) {
			triedToStep++;
			if (mapData[curY+1][curX] == 0 && (mapData[curY+1][curX+1] != 1 || mapData[curY+1][curX-1] != 1)){
				triedToStep = 0;
				madeAStep++;
				curY+=1;
				var currentCell = document.getElementById('row'+curY+'column'+curX);
				if (madeAStep%120 == 0){
					mapData[curY][curX] = 4;
					currentCell.setAttribute('style', 'background-color:green;');
					currentCell.innerHTML = madeAStep;
				} else if (madeAStep%20 == 0){
					mapData[curY][curX] = 2;
					currentCell.setAttribute('style', 'background-color:blue;');
					currentCell.innerHTML = madeAStep;
				} else {
					mapData[curY][curX] = 1;
					currentCell.setAttribute('style', 'background-color:red;');
					currentCell.innerHTML = madeAStep;
				}
			}
		} else if (rightRand > leftRand) {
			triedToStep++;
			if (mapData[curY][curX+1] == 0 && (mapData[curY+1][curX+1] != 1 || mapData[curY-1][curX+1] != 1)){
				triedToStep = 0;
				madeAStep++;
				curX+=1;
				var currentCell = document.getElementById('row'+curY+'column'+curX);
				if (madeAStep%120 == 0){
					mapData[curY][curX] = 4;
					currentCell.setAttribute('style', 'background-color:green;');
					currentCell.innerHTML = madeAStep;
				} else if (madeAStep%20 == 0){
					mapData[curY][curX] = 2;
					currentCell.setAttribute('style', 'background-color:blue;');
					currentCell.innerHTML = madeAStep;
				} else {
					mapData[curY][curX] = 1;
					currentCell.setAttribute('style', 'background-color:red;');
					currentCell.innerHTML = madeAStep;
				}
			}
		} else {
			triedToStep++;
			if (mapData[curY][curX-1] == 0 && (mapData[curY+1][curX-1] != 1 || mapData[curY-1][curX-1] != 1)){
				triedToStep = 0;
				madeAStep++;
				curX-=1;
				var currentCell = document.getElementById('row'+curY+'column'+curX);
				if (madeAStep%120 == 0){
					mapData[curY][curX] = 4;
					currentCell.setAttribute('style', 'background-color:green;');
					currentCell.innerHTML = madeAStep;
				} else if (madeAStep%20 == 0){
					mapData[curY][curX] = 2;
					currentCell.setAttribute('style', 'background-color:blue;');
					currentCell.innerHTML = madeAStep;
				} else {
					mapData[curY][curX] = 1;
					currentCell.setAttribute('style', 'background-color:red;');
					currentCell.innerHTML = madeAStep;
				}
			}
		} 
		if (triedToStep == 10) {
			madeAStep++;
			if (upRand > downRand && upRand > rightRand && upRand > leftRand) {
				curY--;
			} else if (downRand > rightRand && downRand > leftRand) {
				curY++;
			} else if (rightRand > leftRand) {
				curX++;
			} else {
				curX--;
			}
			var currentCell = document.getElementById('row'+curY+'column'+curX);
			if (mapData[curY][curX] != 2 && mapData[curY][curX] != 4 && mapData[curY][curX] != 1 && madeAStep%20 != 0){
				mapData[curY][curX] = 1;
				currentCell.setAttribute('style', 'background-color:red;');
				currentCell.innerHTML = madeAStep;
			} else {

				if (madeAStep%120 == 0){
					mapData[curY][curX] = 4;
					currentCell.setAttribute('style', 'background-color:green;');
					currentCell.innerHTML = madeAStep;
				} else if (madeAStep%20 == 0){
					mapData[curY][curX] = 2;
					currentCell.setAttribute('style', 'background-color:blue;');
					currentCell.innerHTML = madeAStep;
				}

			}
			triedToStep = 0;
		}

		stepCounter++;

	} while ((curY != 0 && curY != mapSize-1) && (curX != 0 && curX != mapSize-1));
	return madeAStep;
}

var goodMap = false;

while (!goodMap) {
	var stepsCounted = generateMap();
	if (stepsCounted > mapSize*8) {
		goodMap = true;
	}
}