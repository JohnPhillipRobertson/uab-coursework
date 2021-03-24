package ch.makery.address.model;

public class Thing {

	public StringBuilder history = new StringBuilder();
	
	public Thing() {
		history.append("");
	}
	
	public String historyProperty() {
		return history.toString();
	}
	
	public void addHistory(String str) {
		history.append("\n");
		history.append(str);
	}

}
