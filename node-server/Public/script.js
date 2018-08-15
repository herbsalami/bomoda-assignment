let data = false;

const toggleData = () => {
	if(data) {
		wipeData();
	}
	else {
		getData();
	}
	data = !data;
}

const wipeData = () => {
	document.getElementById('stats').innerHTML = '';
	document.getElementById('button').innerHTML = '<h3> Click here to see stats </h3>';
}

const getData = () => {
	fetch('/status')
		.then(res => res.json())
		.then((json) => {
			document.getElementById('stats').innerHTML = createDataNodes(json);
			document.getElementById('button').innerHTML = '<h3> Click here to remove stats </h3>';
		})
}

const readabilify = (ugly) => {
	switch (ugly) {
		case 'appRunDuration':
			return 'Duration of Current Process (seconds)';
		case 'firstRequestTimeEver':
			return 'Date/Time First Request Ever Received (epoch)';
		case 'requestsSinceInception':
			return 'Number of Requests Since The Server First Ran';
		case 'requestsSinceStart':
			return 'Number of Requests Since the Current Process Began';
		default:
			return 'Unknown Property';
	}

}

const createDataNodes = (data) => {
	let html = '';
	for (let prop in data) {
		html += `<div class="data-item"><h3>${readabilify(prop)}: \n ${data[prop]}</h3></div>`;
	}
	return html;
}

document.getElementById('button').addEventListener('click', toggleData);