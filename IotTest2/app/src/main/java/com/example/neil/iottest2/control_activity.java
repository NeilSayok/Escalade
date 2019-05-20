package com.example.neil.iottest2;

import android.annotation.SuppressLint;
import android.app.Dialog;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.graphics.drawable.ColorDrawable;
import android.os.AsyncTask;
import android.os.Bundle;
import android.support.annotation.Nullable;
import android.support.design.widget.FloatingActionButton;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.MotionEvent;
import android.view.View;
import android.view.Window;
import android.view.WindowManager;
import android.widget.Button;
import android.widget.ImageButton;
import android.widget.TextView;
import android.widget.Toast;

import com.erz.joysticklibrary.JoyStick;

import java.lang.reflect.Array;
import java.util.Arrays;

public class control_activity extends AppCompatActivity {

    Dialog dialog,d;

    FloatingActionButton clawDialog,liftDialog;

    FloatingActionButton bOne,bTwo,bThree,bFour,bFive,bSix;
    TextView tOne,tTwo,tThree,tFour,tFive,tSix;

    ImageButton dClose;

    Button onOffSwitch;


    //Message Format => On/Off,LJstick,RJsick,LiUP-Down,LiPush-Pull,LiFor-Back,CLOpen-Close,CLUP-Down,ClLft-Right/
    //-1 is no working position
    //0 is off 1 is on
    String msg[] = {"0","-1","-1","-1","-1","-1","-1","-1","-1"};

    boolean onOff = false;


    TcpClient tcpClient;
    String dName = "";
    String SERVER_IP;
    int SERVER_PORT;
    SharedPreferences sp;

    JoyStick joyLeft,joyRight;




    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.joystick_layout);

        sp = getSharedPreferences(getString(R.string.pref_name),MODE_PRIVATE);

        SERVER_IP = sp.getString(getString(R.string.ip),"192.168.0.0");
        SERVER_PORT = sp.getInt(getString(R.string.port),6666);

        Toast.makeText(getApplicationContext(), SERVER_IP + " : " + SERVER_PORT, Toast.LENGTH_SHORT).show();

        new ConnectTask().execute("");

        //Setting Views on base activity;
        clawDialog = findViewById(R.id.clawDialogOpen);
        liftDialog = findViewById(R.id.LiftDialogOpen);
        onOffSwitch = findViewById(R.id.ready);

        clawDialog.setOnClickListener(onClickListener);
        liftDialog.setOnClickListener(onClickListener);
        onOffSwitch.setOnClickListener(onClickListener);

        joyLeft = findViewById(R.id.leftJoyStick);
        joyRight = findViewById(R.id.rightJoyStick);

        joyRight.setType(JoyStick.TYPE_2_AXIS_UP_DOWN);
        joyLeft.setType(JoyStick.TYPE_2_AXIS_LEFT_RIGHT);

        joyLeft.setListener(jLeftListener);
        joyRight.setListener(jRightListener);






    }

    @Override
    protected void onDestroy() {
        super.onDestroy();
        if (tcpClient != null) {
            tcpClient.stopClient();
        }
    }


    private void closeDialog(){
        //Button Setter;
        bOne = null;
        bTwo = null;
        bThree = null;
        bFour = null;
        bFive = null;
        bSix = null;
        //TextView Setter
        tOne = null;
        tTwo = null;
        tThree = null;
        tFour = null;
        tFive = null;
        tSix = null;
        //Dialog Name reset
        dName = "";
        //Dismiss Dialog
        dialog.dismiss();
        //Image Btn
        dClose = null;
    }

    @SuppressLint("ClickableViewAccessibility")
    private void setClickListener(){


        bOne.setOnTouchListener(onTouchListener);
        bTwo.setOnTouchListener(onTouchListener);
        bThree.setOnTouchListener(onTouchListener);
        bFour.setOnTouchListener(onTouchListener);
        bFive.setOnTouchListener(onTouchListener);
        bSix.setOnTouchListener(onTouchListener);


        tOne.setOnTouchListener(onTouchListener);
        tTwo.setOnTouchListener(onTouchListener);
        tThree.setOnTouchListener(onTouchListener);
        tFour.setOnTouchListener(onTouchListener);
        tFive.setOnTouchListener(onTouchListener);
        tSix.setOnTouchListener(onTouchListener);

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
























    JoyStick.JoyStickListener jLeftListener = new JoyStick.JoyStickListener() {
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

    JoyStick.JoyStickListener jRightListener = new JoyStick.JoyStickListener() {
        @Override
        public void onMove(JoyStick joyStick, double angle, double power, int direction) {
            msg[2] = Integer.toString(direction);
            sendMessage();
        }

        @Override
        public void onTap() {

        }

        @Override
        public void onDoubleTap() {

        }
    };


    View.OnClickListener onClickListener = new View.OnClickListener() {
        @Override
        public void onClick(View v) {
            switch (v.getId()){
                case R.id.clawDialogOpen:
                    dialog = new Dialog(control_activity.this,R.style.Noactionbar);
                    dialog.requestWindowFeature(Window.FEATURE_NO_TITLE);
                    dialog.getWindow().setLayout(WindowManager.LayoutParams.MATCH_PARENT, WindowManager.LayoutParams.MATCH_PARENT);
                    dialog.setContentView(R.layout.claw_dialogbox);
                    //Dialog Name
                    dName = "claw";
                    //Button Setter;
                    bOne = dialog.findViewById(R.id.btnOpen);
                    bTwo = dialog.findViewById(R.id.btnClose);
                    bThree = dialog.findViewById(R.id.btnClawUP);
                    bFour = dialog.findViewById(R.id.btnClawDown);
                    bFive = dialog.findViewById(R.id.btnLeft);
                    bSix = dialog.findViewById(R.id.btnRight);
                    //TextView Setter
                    tOne = dialog.findViewById(R.id.txtOpen);
                    tTwo = dialog.findViewById(R.id.txtClose);
                    tThree = dialog.findViewById(R.id.txtClawUP);
                    tFour = dialog.findViewById(R.id.txtClawDown);
                    tFive = dialog.findViewById(R.id.txtLeft);
                    tSix = dialog.findViewById(R.id.txtRight);
                    //Image Btn
                    dClose = dialog.findViewById(R.id.ClawDialogClose);

                    //Setting On Click Listeners
                    setClickListener();
                    dClose.setOnClickListener(dialogBtnOnClick);

                    dialog.show();
                    break;

                case R.id.LiftDialogOpen:
                    dialog = new Dialog(control_activity.this,R.style.Noactionbar);
                    dialog.requestWindowFeature(Window.FEATURE_NO_TITLE);
                    dialog.getWindow().setLayout(WindowManager.LayoutParams.MATCH_PARENT, WindowManager.LayoutParams.MATCH_PARENT);
                    dialog.setContentView(R.layout.lift_dialogbox);
                    //Dialog Name
                    dName = "lift";
                    //Button Setter;
                    bOne = dialog.findViewById(R.id.btnUP);
                    bTwo = dialog.findViewById(R.id.btnDown);
                    bThree = dialog.findViewById(R.id.btnPush);
                    bFour = dialog.findViewById(R.id.btnPull);
                    bFive = dialog.findViewById(R.id.btnForward);
                    bSix = dialog.findViewById(R.id.btnBack);
                    //TextView Setter
                    tOne = dialog.findViewById(R.id.txtUp);
                    tTwo = dialog.findViewById(R.id.txtDown);
                    tThree = dialog.findViewById(R.id.txtPush);
                    tFour = dialog.findViewById(R.id.txtPull);
                    tFive = dialog.findViewById(R.id.txtForward);
                    tSix = dialog.findViewById(R.id.txtBack);
                    //Image Btn
                    dClose = dialog.findViewById(R.id.LiftDialogClose);

                    //Setting On Click Listeners
                    setClickListener();
                    dClose.setOnClickListener(dialogBtnOnClick);


                    dialog.show();
                    break;

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



    View.OnClickListener dialogBtnOnClick = new View.OnClickListener() {
        @Override
        public void onClick(View v) {

            if (v == dClose)
                closeDialog();


        }
    };


    //Message Format => On/Off,LJstick,RJsick,LiUP-Down,LiPush-Pull,LiFor-Back,CLOpen-Close,CLUP-Down,ClLft-Right/
    View.OnTouchListener onTouchListener = new View.OnTouchListener() {
        @Override
        public boolean onTouch(View v, MotionEvent event) {
            if (event.getAction() == MotionEvent.ACTION_DOWN) {

                    if (dName.equals("claw")) {

                        if (v == bOne || v == tOne) {
                            //Claw Open
                            msg[6] = "1";
                            sendMessage();


                        } else if (v == bTwo || v == tTwo) {
                            //Claw Close
                            msg[6] = "2";
                            sendMessage();

                        } else if (v == bThree || v == tThree) {
                            //Claw up
                            msg[7] = "1";
                            sendMessage();


                        } else if (v == bFour || v == tFour) {
                            //Claw down
                            msg[7] = "2";
                            sendMessage();


                        } else if (v == bFive || v == tFive) {
                            //Claw left
                            msg[8] = "1";
                            sendMessage();


                        } else if (v == bSix || v == tSix) {
                            //Claw right
                            msg[8] = "2";
                            sendMessage();


                        }
                        return true;
                    } else if (dName.equals("lift")) {

                        if (v == bOne || v == tOne) {
                            //Lift Up
                            msg[3] = "1";
                            sendMessage();

                        } else if (v == bTwo || v == tTwo) {
                            //Lift Down
                            msg[3] = "2";
                            sendMessage();

                        } else if (v == bThree || v == tThree) {
                            //Lift Push
                            msg[4] = "1";
                            sendMessage();

                        } else if (v == bFour || v == tFour) {
                            //Lift Pull
                            msg[4] = "2";
                            sendMessage();

                        } else if (v == bFive || v == tFive) {
                            //Lift Forward
                            msg[5] = "1";
                            sendMessage();

                        } else if (v == bSix || v == tSix) {
                            //Lift Back
                            msg[5] = "2";
                            sendMessage();

                        }
                    return true;


                }
            }else if (event.getAction() == MotionEvent.ACTION_UP){

                if (dName.equals("claw")){
                    if (v == bOne || v == tOne) {
                        //Claw Open
                        msg[6] = "-1";
                        sendMessage();


                    } else if (v == bTwo || v == tTwo) {
                        //Claw Close
                        msg[6] = "-1";
                        sendMessage();

                    } else if (v == bThree || v == tThree) {
                        //Claw up
                        msg[7] = "-1";
                        sendMessage();


                    } else if (v == bFour || v == tFour) {
                        //Claw down
                        msg[7] = "-1";
                        sendMessage();


                    } else if (v == bFive || v == tFive) {
                        //Claw left
                        msg[8] = "-1";
                        sendMessage();


                    } else if (v == bSix || v == tSix) {
                        //Claw right
                        msg[8] = "-1";
                        sendMessage();


                    }
                }
                else if (dName.equals("lift")){

                    if (v == bOne || v == tOne){
                        //Lift Up Release
                        msg[3] = "-1";
                        sendMessage();

                    }else if (v == bTwo || v == tTwo){
                        //Lift Down Release
                        msg[3] = "-1";
                        sendMessage();

                    }else if (v == bThree || v == tThree){
                        //Lift Push Release
                        msg[4] = "-1";
                        sendMessage();

                    }else if (v == bFour || v == tFour){
                        //Lift Pull release
                        msg[4] = "-1";
                        sendMessage();

                    }else if (v == bFive || v == tFive){
                        //Lift Forward Release
                        msg[5] = "-1";
                        sendMessage();

                    }else if (v == bSix || v == tSix){
                        //Lift Back release
                        msg[5] = "-1";
                        sendMessage();

                    }
                }
                return true;
            }

            return true;
        }
    };



    }


