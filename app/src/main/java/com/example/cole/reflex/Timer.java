package com.example.cole.reflex;

import android.os.CountDownTimer;
import android.view.Gravity;
import android.widget.EditText;
import android.widget.Toast;

public abstract class Timer {



    protected EditText onTickEditText;
    public Toast toastToUse;
    GameMode currentGameMode;

    public Timer(EditText givenTickEditText, Toast toastToUtilize, GameMode givenCurrentGameMode) {

        onTickEditText = givenTickEditText;
        toastToUse = toastToUtilize;
        currentGameMode = givenCurrentGameMode;

    }

    public Timer(EditText onTickEditText, GameMode givenCurrentGameMode) {
        this.onTickEditText = onTickEditText;
        currentGameMode = givenCurrentGameMode;
    }

    protected void timerCountdown(int finishTime, final EditText onTickEditText, final String
                                  onTickGivenText, final GameMode currentGameMode){
        new CountDownTimer(finishTime, 1000) {

            public void onTick(long millisUntilFinished) {

                onTickEditText.setText(onTickGivenText);
            }

            public void onFinish() {

                toastToUse.show();
                currentGameMode.gameModeSetBoolean();
                currentGameMode.clickableButtonStartTime();


            }
        }.start();
    }






    protected void timerCountdown(final EditText onTickEditText, final GameMode currentGameMode){
        new CountDownTimer(6000, 1000) {

            public void onTick(long millisUntilFinished) {

                onTickEditText.setText("Restarting in..." + millisUntilFinished / 1000);
            }

            public void onFinish() {

                toastToUse.show();


            }
        }.start();
    }


}
