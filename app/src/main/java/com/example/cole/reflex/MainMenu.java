package com.example.cole.reflex;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.widget.Button;

public class MainMenu extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main_menu);

        Button singlePlayerModeButton = (Button) findViewById(R.id.singlePlayerModeButton);
        Button multiPlayerModeButton = (Button) findViewById(R.id.multiPlayerModeButton);
        Button statisticsScreenButton = (Button) findViewById(R.id.statisticsScreenButton);

        DataManager dataManager = new DataManager();

        singlePlayerModeButton.setOnClickListener(new View.OnClickListener(){
            public void onClick(View v){ //WhenButtonClicked
                startActivity(new Intent(MainMenu.this, SinglePlayer.class));
            }

        });

        multiPlayerModeButton.setOnClickListener(new View.OnClickListener(){
            public void onClick(View v){ //WhenButtonClicked
                startActivity(new Intent(MainMenu.this, MultiplayerOptions.class));
            }

        });

        statisticsScreenButton.setOnClickListener(new View.OnClickListener(){
            public void onClick(View v){ //WhenButtonClicked
                startActivity(new Intent(MainMenu.this, Statistics.class));
            }

        });



















    }

}
