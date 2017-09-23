var request = new XMLHttpRequest();
request.open('GET','https://learnwebcode.github.io/json-example/animals-1.json');
request.onload = function() {
	var menueListData = JSON.parse(request.responseText);
	console.log(menueListData[0]);
	var ul = document.getElementsByClassName("portal-sidebar-items");
	for(var i =0; i<menueListData.length;i++){
		var li = document.createElement("li");
		li.appendChild(document.createTextNode(menueListData[i].name));
		ul.appendChild(li);
	}
};
request.send();