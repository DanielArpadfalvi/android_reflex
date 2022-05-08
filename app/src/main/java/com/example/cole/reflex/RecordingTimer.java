package com.example.cole.reflex;

import android.widget.EditText;
import android.widget.Toast;

import java.util.Random;

public class RecordingTimer extends Timer{

    String recordingTimerText = "RecordingTimer text";

    public RecordingTimer(EditText givenTickEditText, Toast toastToUse, GameMode currentMode) {
        super(givenTickEditText, toastToUse, currentMode);
    }

    public void beginRecordingTimer(EditText onTickEditText){
        Random rand = new Random();
        int rngDeterminedTime = rand.nextInt(1990);
        rngDeterminedTime = rngDeterminedTime +10;

        super.timerCountdown(rngDeterminedTime, onTickEditText, recordingTimerText,
                currentGameMode);
    }
}
