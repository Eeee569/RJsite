
//populate the page with the menue items and other static content
var menueList = document.getElementsByClassName('portal-sidebar-items')[0].childNodes;
var request = new XMLHttpRequest();
request.open('GET','https://learnwebcode.github.io/json-example/animals-1.json');
request.onload = function() {
	var menueListData = JSON.parse(request.responseText);
	console.log(menueListData[0]);
	var ul = document.getElementsByClassName('portal-sidebar-items')[0];
	for(var i =0; i<menueListData.length;i++){
		var li = document.createElement('li');
		li.appendChild(document.createTextNode(menueListData[i].name));
		li.addEventListener("click",function() { menueClick(li); } ,false);// = menueClick();
		ul.appendChild(li);
	}
	menueList = document.getElementsByClassName('portal-sidebar-items')[0].childNodes;
};
request.send();

//on click request the corisponding item for the page body
function menueClick(menueItem){
	console.log("clicked");
	var mainIframe = document.getElementsByClassName('portal-content-frame')[0];
	mainIframe.src = 'https://math.dartmouth.edu';

}
