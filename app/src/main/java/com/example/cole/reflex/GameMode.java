package com.example.cole.reflex;

import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class GameMode {

    private EditText textLineToModify;
    public Toast toastRecord;
    Button buttonToPress;
    private boolean areWeThereYet;
    long recordedStartTime;
    long recordedEndTime;

    final long[] long_array = new long[1];

    public GameMode(EditText textLine, Toast toast, Button givenButtonToPress) {
        textLineToModify = textLine;
        toastRecord = toast;
        buttonToPress = givenButtonToPress;
    }

    public void gameModeBegin(){
        textLineToModify.setText("Prepare to click!");
        RecordingTimer gameModeTimer = new RecordingTimer(textLineToModify, toastRecord, this);
        gameModeTimer.beginRecordingTimer(textLineToModify);
        buttonToPress.setVisibility(View.VISIBLE);
        areWeThereYet = false;

    }

    public void gameModeSetBoolean(){
        areWeThereYet = true;
    }

    public boolean gameModeGetBoolean(){
        return areWeThereYet;
    }

    public void gameModeDoneTooEarly(){
        textLineToModify.setText("TOO EARLY, FOOL!");
        MisplayTimer misplayTimer = new MisplayTimer(textLineToModify, this);

        misplayTimer.beginMisplayTimer();


    }

    public void gameModeDoneSuccess(){
        textLineToModify.setText("SUCCESS!");
        clickableButtonEndTime();

        long timeDifference = obtainTimeDifference(recordedStartTime, recordedEndTime);
        SingleStatistics singleStatisticsObject = new SingleStatistics(timeDifference);

    }
    public void gameReset(){


    }

    public void clickableButtonStartTime(){
        long buttonStartTime = System.nanoTime();
        recordedStartTime =  buttonStartTime;;
    }
    public void clickableButtonEndTime(){
        long buttonEndTime = System.nanoTime();
        recordedEndTime =  buttonEndTime;
    }

    public long obtainTimeDifference(long startTime, long endTime){
        long howLongItTook = endTime - startTime;
        return(howLongItTook);

    }



}
