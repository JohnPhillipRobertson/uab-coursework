function like() {
	parseInt(document.getElementById('like_number').value);
	//do something here to get the database value, then write an increment to the database
	var db_val = 0; //get from the database
	document.getElementById('like_number').value = db_val;
}