package ch.makery.address.view;

import ch.makery.address.Main;
import ch.makery.address.model.Thing;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.scene.control.Button;
import javafx.scene.control.ChoiceBox;
import javafx.scene.control.ColorPicker;
import javafx.scene.control.TextArea;

public class ThingController {
	
    private String cboption1 = "Element 1";
    private String cboption2 = "Element 2";
    private String cboutput1 = "Element 1 selected";
    private String cboutput2 = "Element 2 selected";
    private String cboutput3 = "Element 1 deleted";
    private String cboutput4 = "Element 2 deleted";
    private Main mainApp;
    private Thing thing = new Thing();
	
    @FXML
    private ColorPicker colorpicker;
    @FXML
    private TextArea textarea;
    @FXML
    private Button selectbutton;
    @FXML
    private Button deletebutton;
    @FXML
    private Button changecolorbutton;
    @FXML
    private ChoiceBox<String> choicebox = new ChoiceBox<String>();
    private ObservableList<String> choices = FXCollections.observableArrayList(cboption1, cboption2);
    
    
    public ThingController() {
    }
    
    private void showThingDetails(String str) {
    	textarea.setText("");
    	thing.addHistory(str);
    	textarea.setText(textarea.getText() + thing.historyProperty());
    }
    
    @FXML
    private void handleSelect() {
    	if (choicebox.getValue().equals(cboption1)) showThingDetails(cboutput1);
		else if (choicebox.getValue().equals(cboption2)) showThingDetails(cboutput2);
    }
    
    @FXML
    private void handleDelete() {
		if (choicebox.getValue().equals(cboption1)) showThingDetails(cboutput3);
		else if (choicebox.getValue().equals(cboption2)) showThingDetails(cboutput4);
    }
    
    @FXML
    private void initialize() {
    	changecolorbutton.setStyle("-fx-background-color: #ff0000; ");
    	choicebox.setItems(choices);
    	textarea.setText(thing.historyProperty());
    	//choicebox.getSelectionModel().selectedItemProperty().addListener((observable, oldValue, newValue) -> showThingDetails());
    }
    
    public void setMainApp(Main mainApp) {
        this.mainApp = mainApp;
    }
    
}
/*
 * https://stackoverflow.com/questions/29673188/appending-text-into-textarea
 * https://docs.oracle.com/javafx/2/ui_controls/choice-box.htm
 * http://www.learningaboutelectronics.com/Articles/How-to-retrieve-data-from-a-ChoiceBox-in-JavaFX.php
 */
