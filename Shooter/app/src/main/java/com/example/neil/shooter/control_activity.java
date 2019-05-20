package com.example.neil.shooter;

import android.annotation.SuppressLint;
import android.content.SharedPreferences;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.design.widget.FloatingActionButton;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

import com.erz.joysticklibrary.JoyStick;

import java.util.Arrays;

public class control_activity extends AppCompatActivity {

    Button onOffSwitch;
    TextView shootT1,shootT2,lTurnT,RturnT;
    FloatingActionButton shootB1,shootB2,lTurnB,RturnB;
    JoyStick movment;

    //ON/OFF,For/bck,fire,lturn/rturn
    String msg[] = {"0","-1","-1","-1"};

    TcpClient tcpClient;
    String dName = "";
    String SERVER_IP;
    int SERVER_PORT;
    SharedPreferences sp;

    boolean onOff = false;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_control);

        sp = getSharedPreferences(getString(R.string.pref_name), MODE_PRIVATE);

        SERVER_IP = sp.getString(getString(R.string.ip), "192.168.43.0");
        SERVER_PORT = sp.getInt(getString(R.string.port), 6666);


        new ConnectTask().execute("");

        onOffSwitch = findViewById(R.id.ready);

        shootT1 = findViewById(R.id.fireTxt1);
        shootB1 = findViewById(R.id.fireBtn1);

        shootT2 = findViewById(R.id.fireTxt2);
        shootB2 = findViewById(R.id.fireBtn2);

        lTurnT = findViewById(R.id.LturnTxt);
        lTurnB = findViewById(R.id.LTurnBtn);

        RturnT = findViewById(R.id.rTurnTxt);
        RturnB = findViewById(R.id.RturnBtn);

        movment = findViewById(R.id.movementJS);

        setListeners();

    }

    @SuppressLint("ClickableViewAccessibility")
    private void setListeners(){
        onOffSwitch.setOnClickListener(onClickListener);

        shootT1.setOnTouchListener(onTouchListener);
        shootT2.setOnTouchListener(onTouchListener);
        shootB1.setOnTouchListener(onTouchListener);
        shootB2.setOnTouchListener(onTouchListener);
        lTurnT.setOnTouchListener(onTouchListener);
        lTurnB.setOnTouchListener(onTouchListener);
        RturnT.setOnTouchListener(onTouchListener);
        RturnB.setOnTouchListener(onTouchListener);

        movment.setType(JoyStick.TYPE_2_AXIS_UP_DOWN);
        movment.setListener(movementListner);
    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (tcpClient != null) {
            tcpClient.stopClient();
        }
    }

    private void sendMessage(){
        String message =  Arrays.toString(msg);
        message = message.substring(1,message.length()-1);
        message = message.replace(", ",",");
        message += "/";

        if (tcpClient != null) {
            tcpClient.sendMessage(message);
        }
        Log.d("Message" ,message);
    }

    JoyStick.JoyStickListener movementListner = new JoyStick.JoyStickListener() {
        @Override
        public void onMove(JoyStick joyStick, double angle, double power, int direction) {
            msg[1] = Integer.toString(direction);
            sendMessage();

        }

        @Override
        public void onTap() {

        }

        @Override
        public void onDoubleTap() {

        }
    };

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

    View.OnClickListener onClickListener = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            switch (v.getId()){
                case R.id.ready:
                    if (!onOff){
                        msg[0] = "1";
                        onOff = true;
                        onOffSwitch.setBackground(getDrawable(R.drawable.rounded_bt_green));
                        onOffSwitch.setText("ON");
                        //Todo send Message
                        sendMessage();
                    }else {
                        msg[0] = "0";
                        onOff = false;
                        onOffSwitch.setBackground(getDrawable(R.drawable.rounded_bt_red));
                        onOffSwitch.setText("OFF");
                        //Todo send Message
                        sendMessage();
                    }

            }
        }
    };


     View.OnTouchListener onTouchListener = new View.OnTouchListener() {
         @Override
         public boolean onTouch(View v, MotionEvent event) {
             if (event.getAction() == MotionEvent.ACTION_DOWN){
                 if (v == shootT1 || v == shootT2 || v == shootB1 || v ==shootB2){
                     //Fire Ball
                     msg[2] = "1";
                     sendMessage();
                 }else if (v == lTurnT || v == lTurnB){
                     //Turn Left
                     msg[3] = "1";
                     sendMessage();
                 }else if (v == RturnT || v == RturnB){
                     //turn Right
                     msg[3] = "2";
                     sendMessage();
                 }
                 return true;
             }else if (event.getAction() == MotionEvent.ACTION_UP){
                 if (v == shootT1 || v == shootT2 || v == shootB1 || v ==shootB2){
                     //Fire Ball
                     msg[2] = "-1";
                     sendMessage();
                 }else if (v == lTurnT || v == lTurnB){
                     //Turn Left
                     msg[3] = "-1";
                     sendMessage();
                 }else if (v == RturnT || v == RturnB){
                     //turn Right
                     msg[3] = "-1";
                     sendMessage();
                 }
                 return true;
             }
         return true;
         }

     };
}