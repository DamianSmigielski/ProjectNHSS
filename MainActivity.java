package com.example.haszerr.cameraapp;

import android.os.Bundle;
import android.app.Activity;
import android.net.Uri;
import android.view.View;
import android.widget.*;
import android.widget.Toast;


public class MainActivity extends Activity {
     VideoView stream ;
     Button connectButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        stream = (VideoView) findViewById(R.id.videoView);
        connectButton =(Button) findViewById(R.id.button);

        MediaController media = new MediaController(this);

        stream.setMediaController((media));

        System.out.println("Starting App");

        connectButton.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                stream.setVideoURI(Uri.parse("http://192.168.0.164:8081/"));
                stream.start();
                Toast.makeText(getApplicationContext(),"Trying to connect",Toast.LENGTH_SHORT).show();
            }
        });
    }


    @Override
    protected void onDestroy() {
        super.onDestroy();

    }

}
