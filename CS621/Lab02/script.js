

//https://stackoverflow.com/a/18470972/9295513
//https://stackoverflow.com/a/9456325/9295513
//https://stackoverflow.com/a/1085810/9295513

function change_op() {
	var operator = document.getElementById("functions").options[document.getElementById("functions").selectedIndex].text;
	var symbol;
	switch (operator) {
		case "Add":
			symbol = " + ";
			break;
		case "Subtract":
			symbol = " - ";
			break;
		case "Multiply":
			symbol = " * ";
			break;
		case "Divide":
			symbol = " / ";
			break;
		case "Exponentiate":
			symbol = " ^ ";
			break;
		default:
			symbol = "";
	}
	document.getElementById("op").innerHTML = symbol;
	if (symbol === "") {
		document.getElementById("b").style.visibility = 'hidden';
	}
	else {
		document.getElementById("b").style.visibility = 'visible';
	}
}
function operate(a, b, operator) {
	switch (operator) {
		case "Add":
			return a + b;
			break;
		case "Subtract":
			return a - b;
			break;
		case "Multiply":
			return a * b;
			break;
		case "Divide":
			return a / b;
			break;

		case "Square Root":
			return Math.sqrt(a);
			break;
		case "Sine":
			return Math.sin(a);
			break;
		case "Cosine":
			return Math.cos(a);
			break;
		case "Tangent":
			return Math.tan(a);
			break;
		case "Exponentiate":
			return Math.pow(a, b);
			break;
		default:
			return NaN;
	}
}
function get_fields() {
	var a = Number(document.getElementById("a").value);
	var b = Number(document.getElementById("b").value);
	var operator = document.getElementById("functions").options[document.getElementById("functions").selectedIndex].text;
	document.getElementById("output").innerHTML = operate(a, b, operator);
}