package com.example.neil.escaladel;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.support.design.widget.TextInputEditText;
import android.support.v7.app.AppCompatActivity;
import android.view.View;
import android.view.animation.Animation;
import android.view.animation.AnimationUtils;
import android.widget.Button;

public class MainActivity extends AppCompatActivity {

    SharedPreferences sp;
    TextInputEditText ip, port;
    Button connect;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        sp = getSharedPreferences(getString(R.string.pref_name),MODE_PRIVATE);

        ip = findViewById(R.id.ipET);
        port = findViewById(R.id.portET);

        connect = findViewById(R.id.connectBtn);

        connect.setOnClickListener(onClickListener);

    }




    View.OnClickListener onClickListener = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            String i = ip.getText().toString();
            String prt = port.getText().toString();
            Animation anim = AnimationUtils.loadAnimation(getApplicationContext(),R.anim.vibrate);

            if (i.equals("")){
                ip.startAnimation(anim);
                ip.requestFocus();
            }else if (prt.equals("")){
                port.startAnimation(anim);
                port.requestFocus();
            }else {
                sp.edit().putString(getString(R.string.ip),i).apply();
                sp.edit().putInt(getString(R.string.port),Integer.parseInt(prt.trim())).apply();
                startActivity(new Intent(MainActivity.this,control_activity.class));
            }
        }
    };
}
