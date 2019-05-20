package com.example.neil.iotapptest1;

import android.content.Context;
import android.os.AsyncTask;
import android.os.Bundle;
import android.os.PersistableBundle;
import android.support.annotation.Nullable;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.erz.joysticklibrary.JoyStick;

public class joystick_activity extends AppCompatActivity{

    JoyStick joyRight,joyLeft;
    Button ready;
    Double powerL = 0.0,powerR = 0.0;
    int dirL = -1,dirR = -1,SERVER_PORT;
    boolean redy = false;
    String tr, out = "",SERVER_IP;
    TcpClient tcpClient;
    Context mCtx;

    @Override
    protected void onCreate( Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.joystick_layout);

        tr = "O,";

        joyLeft = findViewById(R.id.leftJoyStick);
        joyRight = findViewById(R.id.rightJoyStick);
        ready = findViewById(R.id.ready);

        joyRight.setType(JoyStick.TYPE_2_AXIS_UP_DOWN);
        joyLeft.setType(JoyStick.TYPE_2_AXIS_LEFT_RIGHT);

        mCtx = getApplicationContext();
        SERVER_IP = getIntent().getStringExtra("ip");
        SERVER_PORT = getIntent().getIntExtra("port", 8888);
        Toast.makeText(getApplicationContext(), SERVER_IP + " : " + SERVER_PORT, Toast.LENGTH_SHORT).show();

        new ConnectTask().execute("");
        //Log.d("Status",tcpClient.status);



        

        joyLeft.setListener(jLeftListener);
        joyRight.setListener(jRightListener);

        ready.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                redy = !redy;
                if (redy) {
                    ready.setBackground(getResources().getDrawable(R.drawable.rounded_bt_green));
                    tr = "R,";
                }
                else {
                    ready.setBackground(getResources().getDrawable(R.drawable.rounded_bt_red));
                    tr = "O,";
                }
            }
        });


    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (tcpClient != null) {
            tcpClient.stopClient();
        }
    }

    JoyStick.JoyStickListener jLeftListener = new JoyStick.JoyStickListener() {
        @Override
        public void onMove(JoyStick joyStick, double angle, double power, int direction) {
            //Log.d("Joy Left", "angle = "+Double.toString(angle)+", power = "+Double.toString(power)+" , direction = "+Integer.toString(direction));
            powerL = power;
            dirL = direction;
            out = tr + Integer.toString(dirL)+","+Double.toString(powerL)+","+Integer.toString(dirR)+","+Double.toString(powerR)+"/";
            //Log.d("OUTPUT:",out);
            if (tcpClient != null) {
                tcpClient.sendMessage(out);
            }

        }

        @Override
        public void onTap() {

        }

        @Override
        public void onDoubleTap() {

        }
    };

    JoyStick.JoyStickListener jRightListener = new JoyStick.JoyStickListener() {
        @Override
        public void onMove(JoyStick joyStick, double angle, double power, int direction) {
            //Log.d("Joy Right", "angle = "+Double.toString(angle)+", power = "+Double.toString(power)+" , direction = "+Integer.toString(direction));
            powerR = power;
            dirR = direction;
            out = tr + Integer.toString(dirL)+","+Double.toString(powerL)+","+Integer.toString(dirR)+","+Double.toString(powerR)+"/";
            //Log.d("OUTPUT:",out);
            if (tcpClient != null) {
                tcpClient.sendMessage(out);
            }
        }

        @Override
        public void onTap() {

        }

        @Override
        public void onDoubleTap() {

        }
    };
    
    
    
    
    //TCP CODE

    public class ConnectTask extends AsyncTask<String, String, TcpClient> {


        @Override
        protected TcpClient doInBackground(String... message) {

            //we create a TCPClient object
            tcpClient = new TcpClient(new TcpClient.OnMessageReceived() {
                @Override
                //here the messageReceived method is implemented
                public void messageReceived(String message) {
                    //this method calls the onProgressUpdate
                    publishProgress(message);
                }
            },SERVER_IP,SERVER_PORT,findViewById(R.id.superLayout));
            tcpClient.run();

            return null;
        }

        @Override
        protected void onProgressUpdate(String... values) {
            super.onProgressUpdate(values);
            //response received from server
            Log.d("test", "response " + values[0]);
            //process server response here....

        }

    }




}
