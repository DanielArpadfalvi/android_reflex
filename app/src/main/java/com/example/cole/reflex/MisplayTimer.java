package com.example.cole.reflex;

import android.widget.EditText;
import android.widget.Toast;

public class MisplayTimer extends Timer {

    public MisplayTimer(EditText givenTickEditText, GameMode givenCurrentGameMode) {
        super(givenTickEditText, givenCurrentGameMode);
    }

    public void beginMisplayTimer(){
        this.timerCountdown(onTickEditText, currentGameMode);


    }
}
