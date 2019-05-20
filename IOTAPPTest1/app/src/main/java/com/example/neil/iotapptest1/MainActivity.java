package com.example.neil.iotapptest1;

import android.content.Intent;
import android.support.design.widget.TextInputEditText;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    TextInputEditText ip,port;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        ip = findViewById(R.id.ipET);
        port = findViewById(R.id.portET);
    }

 public void connectBTNpress(View v){

        if (ip.getText().toString().equals("")){
            Toast.makeText(getApplicationContext(),"IP Field is empty",Toast.LENGTH_LONG).show();
            findViewById(R.id.ipTIL).startAnimation(AnimationUtils.loadAnimation(getApplicationContext(),R.anim.vibrate));
        }
        else if (port.getText().toString().equals("")){
            Toast.makeText(getApplicationContext(),"Port Field is empty",Toast.LENGTH_LONG).show();
            findViewById(R.id.ipTIL).startAnimation(AnimationUtils.loadAnimation(getApplicationContext(),R.anim.vibrate));
        }
        else{
            Intent i = new Intent(MainActivity.this,joystick_activity.class);
            i.putExtra("ip",ip.getText().toString());
            i.putExtra("port",Integer.parseInt(port.getText().toString().trim()));
            startActivity(i);
        }

    }






}
